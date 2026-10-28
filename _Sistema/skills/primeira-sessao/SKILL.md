---
name: primeira-sessao
description: Instala o segundo cérebro com o dono numa conversa de 40 minutos e preenche a constituição, o foco e a área da corretora. Use quando o cofre é novo, quando a CONSTITUICAO.md ainda tem campos a preencher ou quando o dono disser vamos instalar.
---

# Primeira sessão

**Quando:** a primeira conversa com o cofre, ou sempre que a `CONSTITUICAO.md` ainda tiver "a preencher" na seção 1 · **Duração:** 40 minutos, no máximo 50 · **Saída:** constituição e foco preenchidos com as palavras do dono, e a área da corretora começada

## Antes de começar

1. Rode `git pull`. Confira com `gh repo view --json visibility` que o repositório é privado. Se for público, pare e explique ao dono como deixar privado: no GitHub, Settings, depois Danger Zone, depois Change visibility, depois Make private.
2. Leia `AGENTS.md`, `CONSTITUICAO.md`, `FOCO.md` e `2_Areas/corretora/visao-geral.md`.
3. Diga ao dono, em três frases curtas, o que vai acontecer: uma conversa de uns 40 minutos, uma pergunta por vez, e no fim o cofre já sabe quem ele é e o que importa agora. Pergunte se ele prefere responder falando (ditado) ou escrevendo.

## As regras da conversa

1. **Uma pergunta por vez.** Nunca mande a lista.
2. **Escute antes da próxima.** Se ele abrir um assunto que importa, siga ele. O roteiro é rede, não trilho.
3. **"Não sei" encerra o assunto.** Fica "a preencher" e a conversa segue.
4. **Grave a cada três ou quatro respostas,** no arquivo certo, para nada se perder se a conversa cair.
5. **Use as palavras dele.** Sua leitura, se houver, vai num bloco marcado "leitura do agente".
6. **Número sem fonte é estimativa.** "Uns 600 clientes" vira "≈600 clientes (estimativa do dono)".
7. **Nada de CPF, apólice, dado bancário ou saúde de cliente.** Se ele começar a ditar, avise com gentileza que isso fica no sistema de gestão.

## Bloco 1 · você (10 minutos) → `CONSTITUICAO.md` §1 e `2_Areas/`

1. Como você se chama e em que cidade trabalha?
2. Além da corretora, você toca alguma outra frente? Outro negócio, outro trabalho, um projeto pessoal grande?
3. Como é a sua semana hoje, de verdade: onde vai a maior parte do seu tempo?
4. Tem alguma coisa da vida pessoal que o agente precisa respeitar? Um dia sagrado, um horário em que não se marca nada.

Para cada frente nova, crie a subpasta em `2_Areas/` com um `visao-geral.md` no mesmo molde da corretora.

## Bloco 2 · a corretora (15 minutos) → `2_Areas/corretora/visao-geral.md` e `3_Referencias/seguradoras/`

1. Desde quando você é corretor, e quem trabalha com você hoje?
2. Em quais ramos está o grosso da sua carteira?
3. Quantos clientes, mais ou menos? Pode ser chute, eu marco como estimativa.
4. Com quais seguradoras você mais trabalha?
5. Que sistema de gestão você usa, e onde ficam os documentos dos clientes?
6. Onde você controla as renovações hoje: sistema, planilha ou cabeça?
7. Qual tarefa repetida mais rouba o seu tempo?
8. O que mais dói quando você pensa na corretora?

Crie uma ficha em `3_Referencias/seguradoras/` para cada seguradora citada, só com o nome e os ramos. O resto entra com o tempo.

## Bloco 3 · o nosso combinado (10 minutos) → `CONSTITUICAO.md` §2, §3 e §4

1. Como você quer que eu fale com você: mais curto ou mais explicado? Você ou senhor?
2. O que você quer que eu **nunca** faça?
3. O que você quer que eu faça mesmo sem você pedir?
4. Onde ficam as coisas que não estão aqui: e-mail principal, pasta de documentos, planilha?

As respostas 2 e 3 viram regra na constituição na mesma hora, com as palavras dele.

## Bloco 4 · o foco (5 minutos) → `FOCO.md`

1. Se as próximas quatro semanas derem certo, o que terá acontecido?
2. Quais são as três coisas mais importantes desta semana? E qual é o gargalo de cada uma?
3. Tem alguma ideia boa que você quer deixar guardada para depois, sem esquecer?

## Para fechar

1. Troque todo "a preencher" que foi respondido. O que não foi respondido continua marcado, e está certo assim.
2. Escreva no topo de `Decisoes/registro.md`: `AAAA-MM-DD · [cofre] Segundo cérebro instalado, com a primeira sessão feita. Dono.`
3. Crie `Diario/AAAA-MM-DD.md` com o que foi gravado, onde, e o que ficou em aberto.
4. Grave no GitHub: `git add -A`, `git commit -m "Primeira sessão: constituição, foco e corretora"`, `git push`.
5. Diga ao dono o que ficou gravado, em no máximo cinco linhas, e a próxima ação: amanhã de manhã, abrir o agente nesta pasta e dizer "bom dia".

## Regras

- Passou de 50 minutos, pare onde estiver, grave e marque no diário onde parou.
- Nunca encha campo com suposição para o arquivo parecer completo.
- Se o dono não for corretor, troque "corretora" pela frente de trabalho dele em todos os arquivos e renomeie a pasta `2_Areas/corretora/`.
