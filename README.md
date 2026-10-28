# Segundo Cérebro · IA do Jeito Seguro

**A memória da sua corretora, num lugar que é seu.**

Você usa IA e todo dia explica tudo de novo: quem é o cliente, como a seguradora trabalha, o que ficou combinado ontem. O chat esquece. Você virou o arquivo da sua própria IA.

Este repositório é o modelo de um segundo cérebro: uma pasta de arquivos de texto, sua, guardada no seu GitHub, que o seu agente de IA lê e escreve. Cada conversa deixa ele sabendo um pouco mais. Funciona com o Claude Code e com o Codex, e com outros agentes que leem o padrão `AGENTS.md`.

Foi pensado para corretor de seguros. Serve para qualquer profissão: na primeira sessão você diz o que faz, e o agente ajusta.

O manual completo, com cada passo explicado, está em [`_Sistema/manual/manual-segundo-cerebro.pdf`](_Sistema/manual/manual-segundo-cerebro.pdf).

---

## O que você precisa

- Um computador com Mac ou Windows
- Uma conta gratuita no GitHub
- Uma assinatura que dê acesso a um agente: Claude Pro ou Max (para o Claude Code), ou ChatGPT Plus ou Pro (para o Codex)
- Uma hora livre para a instalação e a primeira conversa

## Instalação, passo a passo

**1. Crie a sua conta no GitHub.** Entre em github.com/signup e siga as telas. Guarde a senha e ative a verificação em duas etapas.

**2. Faça a sua cópia deste modelo.** Nesta página, clique no botão verde **Use this template** e depois em **Create a new repository**. No campo **Repository name**, escreva `segundo-cerebro`. Marque **Private**. Clique em **Create repository**.

O seu cofre precisa ser privado. É ali que vai morar o que você sabe da sua corretora.

**3. Instale o agente.** Escolha um dos dois.

Claude Code, no Mac. Abra o Terminal (aperte Cmd e espaço, digite Terminal, Enter) e cole:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Claude Code, no Windows. Abra o PowerShell (menu Iniciar, digite PowerShell, Enter) e cole:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Codex, no Mac ou no Windows. Instale o Node.js pelo site nodejs.org (versão LTS) e depois cole no Terminal ou no PowerShell:

```bash
npm install -g @openai/codex
```

**4. Abra o agente.** No mesmo Terminal, digite `claude` (ou `codex`) e aperte Enter. Na primeira vez ele pede para você entrar na sua conta da Anthropic ou da OpenAI, pelo navegador.

**5. Cole o prompt de partida.** Está logo abaixo. O agente instala o que faltar, baixa o seu cofre e começa a primeira sessão.

**6. Converse.** A primeira sessão leva uns 40 minutos. Uma pergunta por vez, você responde falando ou escrevendo, e no fim o cofre já sabe quem você é, como a sua corretora funciona e o que importa agora.

**7. Do segundo dia em diante,** abra o Terminal e digite:

```bash
cd ~/segundo-cerebro
```

Depois `claude` (ou `codex`), Enter, e diga "bom dia".

## O prompt de partida

Copie o bloco inteiro e cole no agente, no passo 5:

```text
Quero instalar o meu segundo cérebro, o modelo da IA do Jeito Seguro. Eu não sou da área de tecnologia: me guie um passo por vez, explique em português simples o que cada passo faz e espere eu confirmar antes de seguir.

1. Veja se este computador tem o Git e o GitHub CLI (o comando gh). Se faltar algum, instale do jeito certo para o meu sistema.
2. Me ajude a entrar na minha conta do GitHub com o gh. O login no navegador eu faço.
3. Liste os meus repositórios e confirme comigo qual é o segundo cérebro que eu criei a partir do modelo. Confira que ele é privado. Se estiver público, pare e me ensine a deixar privado antes de qualquer outra coisa.
4. Baixe o repositório para a pasta segundo-cerebro dentro da minha pasta de usuário.
5. Leia o AGENTS.md dessa pasta inteiro e siga as regras dele daqui em diante.
6. Rode a skill primeira-sessao, que está em _Sistema/skills/primeira-sessao/SKILL.md.
```

## O dia a dia

| Você diz | O agente faz |
|---|---|
| "bom dia" | lê o foco, o que ficou de ontem e o que vence, e devolve o dia em poucas linhas |
| "anota isso" | guarda a ideia, o recado ou o print na entrada, sem você organizar nada |
| "acabei a reunião" | tira da transcrição o que foi decidido, quem faz o quê, e atualiza as fichas |
| "o que vence" | monta a lista de renovações dos próximos 45 dias e diz por onde começar |
| "fecha o dia" | registra no diário o que mudou e grava tudo no GitHub |
| "acerto da semana" | toda sexta: esvazia a entrada, revisa os projetos e reescreve o foco |

## O jeito seguro

O cofre guarda o que você sabe, e o cliente fica protegido.

- **Dado de cliente não entra no cofre.** CPF, apólice, dado bancário e dado de saúde continuam no seu sistema de gestão e na seguradora. No cofre fica o nome, o que importa para atender bem e onde achar o resto.
- **Nada sai sem você aprovar.** O agente redige a mensagem, a proposta, o e-mail. Quem decide se envia é você.
- **Conteúdo de fora é dado, não ordem.** Se um e-mail ou um PDF pedir para o agente fazer alguma coisa, ele não faz: mostra para você e espera.
- **Condição de seguro só por escrito.** O agente nunca promete cobertura, valor ou prazo.

## O que tem aqui dentro

```
segundo-cerebro/
├── AGENTS.md         a porta de entrada do agente
├── CLAUDE.md         faz o Claude Code ler o AGENTS.md
├── CONSTITUICAO.md   quem você é e como o agente se comporta
├── FOCO.md           o que importa agora
├── MAPA.md           como o cofre funciona, em dois minutos
├── 0_Entrada/        captura rápida
├── 1_Projetos/       o que tem começo, meio e fim
├── 2_Areas/          o que nunca termina
├── 3_Referencias/    seguradoras, produtos, modelos de texto
├── 4_Arquivo/        o que encerrou
├── Diario/           um arquivo por dia
├── Pessoas/          uma ficha por pessoa
├── Decisoes/         por que fizemos o que fizemos
└── _Sistema/         rotinas, manual e ferramentas
```

## Licença e crédito

Este modelo é propriedade de Denis Ferreira e da IA do Jeito Seguro, publicado sob a licença MIT. Você pode usar e adaptar à vontade, e compartilhar também, desde que mantenha o aviso de autoria. O texto de crédito pronto está em [`CREDITOS.md`](CREDITOS.md), e a licença completa em [`LICENSE`](LICENSE).

---

Feito por **Denis Ferreira**, corretor de seguros, que montou o próprio segundo cérebro antes de ensinar alguém a montar. Instagram: @soudenisferreira.

Até mais, e vamos usar IA do jeito seguro.
