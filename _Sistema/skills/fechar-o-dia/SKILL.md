---
name: fechar-o-dia
description: Registra no diário o que mudou na conversa, o que foi decidido e o que ficou pendente, e grava no GitHub. Use no fim de toda conversa em que algo mudou, ou quando o dono disser fecha o dia.
---

# Fechar o dia

**Quando:** no fim de toda conversa em que algo mudou, mesmo sem o dono pedir, e quando ele disser "fecha o dia" · **Saída:** o diário de hoje atualizado e tudo no GitHub

## Faz

1. Abra ou crie `Diario/AAAA-MM-DD.md`.
2. Acrescente, na seção "Ao longo do dia", o que aconteceu nesta conversa em até cinco linhas: o que foi feito, o que foi decidido, o que ficou pendente e com quem.
3. Decisão que mudou rumo, custou dinheiro ou criou compromisso também vira linha no topo de `Decisoes/registro.md`.
4. Pessoa citada com novidade: atualize a ficha em `Pessoas/`.
5. `git add -A`, `git commit` com mensagem em português, `git push`.
6. Responda em uma linha dizendo o que ficou gravado e onde.

## Regras

- Registre fato, não opinião. A sua leitura, se houver, vai marcada como leitura.
- Próximo passo sem dono e sem prazo é conversa, não tarefa. Registre como conversa.
- Nunca grave CPF, apólice ou dado de saúde de cliente.
