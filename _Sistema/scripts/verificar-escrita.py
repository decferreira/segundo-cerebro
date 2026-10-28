#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar-escrita.py

Verificador de escrita humana do Segundo Cérebro, IA do Jeito Seguro.
Copyright (c) 2026 Denis Ferreira, IA do Jeito Seguro. Licença MIT, ver LICENSE.
Regra resumida: AGENTS.md, seção 6.

Uso:
    python3 verificar-escrita.py arquivo.md
    python3 verificar-escrita.py pasta/ --ext .md
    cat mensagem.txt | python3 verificar-escrita.py
    python3 verificar-escrita.py arquivo.md --canal whatsapp
    python3 verificar-escrita.py arquivo.md --quieto      (so o placar)

Codigo de saida: 0 se passou, 1 se encontrou problema grave.
Nao depende de nada alem da biblioteca padrao.
"""

import sys
import os
import re
import argparse
import statistics
import unicodedata

# ---------------------------------------------------------------- utilidades

COR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

def c(txt, cod):
    return "\033[%sm%s\033[0m" % (cod, txt) if COR else txt

def vermelho(t): return c(t, "31")
def amarelo(t):  return c(t, "33")
def verde(t):    return c(t, "32")
def cinza(t):    return c(t, "90")
def negrito(t):  return c(t, "1")


# ------------------------------------------------------------------ achados

class Achado:
    def __init__(self, linha, trecho, categoria, peso, sugestao):
        self.linha = linha
        self.trecho = trecho
        self.categoria = categoria
        self.peso = peso          # 3 grave, 2 medio, 1 leve
        self.sugestao = sugestao


# --------------------------------------------------------------- detectores

TRAVESSAO = re.compile(r"[—–]")
# Faixa nao e travessao. O traco medio entre dois numeros, dois horarios,
# dois meses ou dois codigos curtos quer dizer "de X a Y", e esse e o
# caractere certo para isso. A regra da escrita humana mira o travessao
# usado como pausa retorica, nao a faixa.
FAIXA = re.compile(
    r"(?<=[0-9A-Za-zÀ-ÿ])–(?=[0-9A-Za-zÀ-ÿ])"
)

NEGATIVO = [
    (re.compile(r"\bn[ãa]o\s+(?:é|e)\s+(?:apenas|só|somente)\b.{0,60}?,\s*(?:é|e)\b", re.I),
     'paralelismo negativo do tipo "não é apenas X, é Y"'),
    (re.compile(r"\bn[ãa]o\s+(?:apenas|só|somente)\b.{0,80}?\bmas\s+tamb[ée]m\b", re.I),
     'estrutura "não apenas... mas também"'),
    (re.compile(r"\bmais\s+(?:do\s+)?que\s+(?:um|uma)\b.{0,50}?,\s*(?:é|e|um|uma)\b", re.I),
     'reframe "mais que um X, um Y"'),
    (re.compile(r"\bisso\s+n[ãa]o\s+[ée]\b.{0,40}?\.\s*[ÉE]\b", re.I),
     'contraste em duas frases, "Isso não é X. É Y."'),
]

MOLDURAS = [
    "além disso", "por outro lado", "em suma", "em conclusão", "em resumo",
    "vale ressaltar", "vale destacar", "vale lembrar", "vale mencionar",
    "é importante destacar", "é importante ressaltar", "é importante notar",
    "é importante lembrar", "cabe ressaltar", "no mundo de hoje",
    "nos dias atuais", "nos dias de hoje", "atualmente, no",
    "em um cenário cada vez mais", "num cenário cada vez mais",
    "a chave é", "a chave está", "o segredo está", "o segredo é",
    "em última análise", "de modo geral", "em geral, podemos",
    "dito isso", "posto isso", "por fim, é",
]

VOCABULARIO = [
    "potencializar", "potencialize", "alavancar", "alavanque", "robusto",
    "robusta", "transformador", "transformadora", "disruptivo", "disruptiva",
    "jornada", "panorama", "mergulhar", "mergulho profundo", "aprofundar-se",
    "desbloquear", "empoderar", "sinergia", "holístico", "holística",
    "otimizar", "otimize", "impactar", "impactante", "elevar o patamar",
    "no que tange", "no tocante a", "supracitado", "outrossim",
    # ingles, quando o texto for em ingles
    "delve", "tapestry", "pivotal", "testament to", "foster a",
    "seamless", "leverage the", "unlock the", "harness the",
]

ENFASE = [
    "é fundamental", "é crucial", "é essencial", "é vital",
    "peça-chave", "peça chave", "verdadeiro testemunho",
    "não é à toa", "sem dúvida alguma", "com certeza absoluta",
]

ANALISE_RASA = [
    "destacando a importância", "refletindo o compromisso", "ilustrando como",
    "evidenciando a", "reforçando a importância", "demonstrando o compromisso",
    "o que reflete", "o que evidencia", "servindo como",
]

RESIDUO = [
    "espero que ajude", "espero que isso ajude", "claro! aqui está",
    "claro, aqui está", "segue abaixo", "vamos lá!", "ótima pergunta",
    "como modelo de linguagem", "como uma ia", "espero que esta mensagem",
    "fico à disposição para qualquer dúvida adicional",
]

AMPLITUDE = [
    (re.compile(r"\bdesde\s+.{3,40}?\s+at[ée]\s+", re.I), 'falsa amplitude "desde... até..."'),
    (re.compile(r"\bd(?:e|esde)\s+(?:pequenas?|grandes?|simples)\b.{0,40}?\s+a(?:t[ée])?\s+", re.I),
     'falsa amplitude "de pequenas a grandes"'),
    (re.compile(r"\bvariando\s+de\b.{0,40}?\ba\b", re.I), 'falsa amplitude "variando de X a Y"'),
]

# tres itens em serie: palavra, palavra e palavra
TRINCA = re.compile(
    r"\b([a-zçãáàâéêíóôõúü]{4,}),\s+([a-zçãáàâéêíóôõúü]{4,})\s+e\s+([a-zçãáàâéêíóôõúü]{4,})\b"
)

EMOJI = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F000-\U0001F0FF"
    "]"
)

ASPAS_CURVAS = re.compile(r"[“”‘’]")

TITULO_MD = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
TABELA_MD = re.compile(r"^\s*\|")
META_MD = re.compile(r"^\*\*[^*]+:\*\*")
CODIGO_MD = re.compile(r"^\s*```")

PALAVRAS_MINUSCULAS = {
    "de", "da", "do", "das", "dos", "e", "ou", "a", "o", "as", "os",
    "em", "no", "na", "nos", "nas", "para", "por", "com", "um", "uma",
}


def sem_acento(t):
    return "".join(ch for ch in unicodedata.normalize("NFD", t)
                   if unicodedata.category(ch) != "Mn")


def eh_title_case(titulo):
    """Titulo em portugues com quase toda inicial maiuscula."""
    palavras = [p for p in re.findall(r"[A-Za-zÀ-ÿ]+", titulo) if len(p) > 1]
    if len(palavras) < 3:
        return False
    maiusculas = 0
    candidatas = 0
    for p in palavras[1:]:
        if p.lower() in PALAVRAS_MINUSCULAS:
            continue
        candidatas += 1
        if p[0].isupper():
            maiusculas += 1
    return candidatas >= 2 and maiusculas == candidatas


# ------------------------------------------------------------------- analise

def analisar(texto, canal="geral"):
    achados = []
    linhas = texto.split("\n")
    dentro_codigo = False

    for i, linha in enumerate(linhas, 1):
        if CODIGO_MD.match(linha):
            dentro_codigo = not dentro_codigo
            continue
        if dentro_codigo:
            continue

        crua = linha.strip()
        if not crua:
            continue

        # trecho entre crase e codigo literal: nome de arquivo, comando,
        # identificador de terceiro. Nao se julga a escrita de dentro dele.
        crua = re.sub(r"`[^`]*`", "``", crua)

        baixa = crua.lower()
        baixa_sa = sem_acento(baixa)
        em_tabela = bool(TABELA_MD.match(linha))
        em_meta = bool(META_MD.match(crua))

        # travessao
        sem_faixa = FAIXA.sub("\u00a0", crua)
        if TRAVESSAO.search(sem_faixa):
            if canal == "whatsapp" or not (em_tabela or em_meta):
                achados.append(Achado(
                    i, TRAVESSAO.sub(lambda m: "[" + m.group(0) + "]", sem_faixa)[:110],
                    "travessão", 3,
                    "troque por vírgula, parênteses, dois pontos ou ponto final"))

        # paralelismo negativo
        for rx, nome in NEGATIVO:
            m = rx.search(crua)
            if m:
                achados.append(Achado(i, m.group(0)[:110], nome, 3,
                                      "escreva a afirmação direta, sem o contraste"))

        # molduras
        for exp in MOLDURAS:
            if exp in baixa or sem_acento(exp) in baixa_sa:
                achados.append(Achado(i, exp, "moldura de redação", 2,
                                      "corte a expressão, a frase costuma funcionar sem ela"))

        # vocabulario
        for exp in VOCABULARIO:
            if re.search(r"\b" + re.escape(sem_acento(exp)), baixa_sa):
                achados.append(Achado(i, exp, "vocabulário de IA", 2,
                                      "use a palavra simples equivalente"))

        # enfase vazia
        for exp in ENFASE:
            if exp in baixa or sem_acento(exp) in baixa_sa:
                achados.append(Achado(i, exp, "ênfase vazia", 2,
                                      "mostre por que importa, em vez de dizer que importa"))

        # analise rasa
        for exp in ANALISE_RASA:
            if exp in baixa or sem_acento(exp) in baixa_sa:
                achados.append(Achado(i, exp, "análise superficial", 2,
                                      "explique a relevância concreta ou corte"))

        # residuo de chat
        for exp in RESIDUO:
            if exp in baixa or sem_acento(exp) in baixa_sa:
                achados.append(Achado(i, exp, "resíduo de conversa com modelo", 3,
                                      "apague, isso nunca deveria sair"))

        # falsa amplitude
        for rx, nome in AMPLITUDE:
            m = rx.search(crua)
            if m:
                achados.append(Achado(i, m.group(0)[:110], nome, 2,
                                      "diga o caso concreto em vez do intervalo"))

        # regra dos tres
        if not em_tabela:
            for m in TRINCA.finditer(baixa_sa):
                achados.append(Achado(i, m.group(0)[:110], "regra dos três", 2,
                                      "use dois itens ou quatro, a tríade é marca de modelo"))

        # emoji em titulo
        mt = TITULO_MD.match(linha)
        if mt:
            if EMOJI.search(mt.group(1)):
                achados.append(Achado(i, mt.group(1)[:80], "emoji em título", 2,
                                      "tire o emoji do título"))
            if eh_title_case(mt.group(1)):
                achados.append(Achado(i, mt.group(1)[:80], "Title Case em português", 2,
                                      "só a primeira palavra e nomes próprios em maiúscula"))

        # aspas curvas
        if ASPAS_CURVAS.search(crua):
            achados.append(Achado(i, "aspas tipográficas", "aspas curvas", 1,
                                  "use aspas retas, como o teclado produz"))

        # negrito demais
        n_neg = crua.count("**") // 2
        if n_neg >= 4 and not em_tabela:
            achados.append(Achado(i, "%d trechos em negrito nesta linha" % n_neg,
                                  "negrito em excesso", 2,
                                  "negrito serve para uma coisa por bloco, não para termos soltos"))

    # ---------------------------------------------------- metricas de ritmo
    corpo = "\n".join(l for l in linhas
                      if not TABELA_MD.match(l) and not l.strip().startswith("#")
                      and not l.strip().startswith("|"))
    corpo = re.sub(r"```.*?```", " ", corpo, flags=re.S)
    frases = [f.strip() for f in re.split(r"(?<=[.!?])\s+|\n\n", corpo) if len(f.strip()) > 12]
    tamanhos = [len(f.split()) for f in frases]

    metricas = {}
    if len(tamanhos) >= 4:
        metricas["frases"] = len(tamanhos)
        metricas["media"] = round(statistics.mean(tamanhos), 1)
        metricas["desvio"] = round(statistics.pstdev(tamanhos), 1)

        if metricas["desvio"] < 5 and metricas["media"] > 12:
            achados.append(Achado(0, "desvio %.1f palavras" % metricas["desvio"],
                                  "ritmo uniforme", 3,
                                  "as frases têm todas o mesmo tamanho, quebre com uma bem curta"))

        # sequencia de tres frases parecidas
        for k in range(len(tamanhos) - 2):
            a, b, cc = tamanhos[k], tamanhos[k+1], tamanhos[k+2]
            if a > 10 and max(a, b, cc) - min(a, b, cc) <= 3:
                achados.append(Achado(0, "%d, %d e %d palavras" % (a, b, cc),
                                      "três frases seguidas do mesmo tamanho", 2,
                                      "corte uma delas pela metade"))
                break

    texto_puro = re.sub(r"[#*`|>\-]", " ", corpo)
    palavras = len(texto_puro.split())
    if palavras > 60:
        virgulas = texto_puro.count(",")
        metricas["virgulas_por_100"] = round(virgulas / palavras * 100, 1)
        if metricas["virgulas_por_100"] < 2.5:
            achados.append(Achado(0, "%.1f vírgulas por 100 palavras" % metricas["virgulas_por_100"],
                                  "pontuação escassa", 2,
                                  "texto humano respira mais, use vírgula e parênteses"))
        es = len(re.findall(r"\be\b", texto_puro.lower()))
        metricas["e_por_100"] = round(es / palavras * 100, 1)
        if metricas["e_por_100"] > 4.5:
            achados.append(Achado(0, "%.1f ocorrências de 'e' por 100 palavras" % metricas["e_por_100"],
                                  "excesso da conjunção 'e'", 2,
                                  "separe em frases menores em vez de emendar"))

    return achados, metricas


# ------------------------------------------------------------------ relatorio

def relatar(nome, achados, metricas, quieto=False):
    graves = [a for a in achados if a.peso == 3]
    medios = [a for a in achados if a.peso == 2]
    leves = [a for a in achados if a.peso == 1]
    nota = max(0, 100 - (len(graves) * 12 + len(medios) * 5 + len(leves) * 2))

    print()
    print(negrito(nome))
    if metricas:
        partes = []
        if "frases" in metricas:
            partes.append("%d frases, média %s palavras, desvio %s"
                          % (metricas["frases"], metricas["media"], metricas["desvio"]))
        if "virgulas_por_100" in metricas:
            partes.append("%s vírgulas/100 palavras" % metricas["virgulas_por_100"])
        if partes:
            print(cinza("  " + " · ".join(partes)))

    if not achados:
        print(verde("  Limpo. Nenhum padrão encontrado."))
        print()
        return nota, 0

    if not quieto:
        for a in sorted(achados, key=lambda x: (-x.peso, x.linha)):
            marca = vermelho("grave") if a.peso == 3 else (amarelo("médio") if a.peso == 2 else cinza("leve "))
            onde = ("linha %-4d" % a.linha) if a.linha else "texto todo"
            print("  %s  %s  %s" % (marca, cinza(onde), negrito(a.categoria)))
            print("         %s" % a.trecho)
            print(cinza("         → %s" % a.sugestao))
        print()

    cor_nota = verde if nota >= 85 else (amarelo if nota >= 65 else vermelho)
    print("  %d grave(s), %d médio(s), %d leve(s)   placar: %s"
          % (len(graves), len(medios), len(leves), cor_nota(str(nota) + "/100")))
    print()
    return nota, len(graves)


def main():
    ap = argparse.ArgumentParser(
        description="Verifica padrões de escrita de IA. Regra em AGENTS.md, seção 6")
    ap.add_argument("caminhos", nargs="*", help="arquivo ou pasta. Vazio lê da entrada padrão.")
    ap.add_argument("--ext", default=".md", help="extensão ao varrer pasta (padrão .md)")
    ap.add_argument("--canal", default="geral", choices=["geral", "whatsapp"],
                    help="whatsapp aplica o rigor máximo, inclusive em tabela")
    ap.add_argument("--quieto", action="store_true", help="mostra só o placar")
    args = ap.parse_args()

    alvos = []
    if not args.caminhos:
        texto = sys.stdin.read()
        alvos.append(("(entrada padrão)", texto))
    else:
        for p in args.caminhos:
            if os.path.isdir(p):
                for raiz, _, arquivos in os.walk(p):
                    if "/." in raiz:
                        continue
                    for f in sorted(arquivos):
                        if f.endswith(args.ext):
                            cam = os.path.join(raiz, f)
                            with open(cam, encoding="utf-8", errors="replace") as fh:
                                alvos.append((cam, fh.read()))
            elif os.path.isfile(p):
                with open(p, encoding="utf-8", errors="replace") as fh:
                    alvos.append((p, fh.read()))
            else:
                print(vermelho("não encontrei: %s" % p))

    if not alvos:
        print("nada para verificar")
        return 0

    total_graves = 0
    notas = []
    for nome, texto in alvos:
        achados, metricas = analisar(texto, canal=args.canal)
        nota, graves = relatar(nome, achados, metricas, quieto=args.quieto)
        notas.append(nota)
        total_graves += graves

    if len(alvos) > 1:
        print(negrito("  %d arquivos · placar médio %d/100 · %d problema(s) grave(s)"
                      % (len(alvos), sum(notas) / len(notas), total_graves)))
        print()

    return 1 if total_graves else 0


if __name__ == "__main__":
    sys.exit(main())
