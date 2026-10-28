---
name: bom-dia
description: Lê o foco, o diário de ontem, os projetos e o que vence, e devolve o dia do dono em até 15 linhas. Use quando ele disser bom dia, o que tem hoje, ou abrir a primeira conversa de um dia útil.
---

# Bom dia

**Quando:** a primeira conversa de um dia útil, ou quando o dono disser "bom dia" · **Saída:** o dia lido, em até 15 linhas, e o mesmo resumo gravado no diário

## Lê

1. `git pull`
2. `FOCO.md`
3. `Diario/` de ontem e de hoje, se já existir
4. `0_Entrada/`, só para contar quantos itens há e há quanto tempo
5. Os `README.md` de `1_Projetos/`, olhando os próximos passos com data para hoje ou atrasados
6. A fonte de renovações registrada na `CONSTITUICAO.md` §4, se você tiver acesso a ela

## Faz

1. Separe o que é de hoje, o que está atrasado e o que vence nos próximos sete dias.
2. Confronte com o P1 do foco: o dia de hoje serve a ele?
3. Procure os sinais de alerta: entrada com mais de 20 itens, foco com mais de 10 dias, projeto parado há 14 dias.

## Entrega

```
Bom dia. Hoje é <dia da semana>, <data>.

O que importa hoje
1. ...
2. ...

Atrasado
- ...

Vence nesta semana
- ...

Uma sugestão: <a coisa que mais destrava o P1 hoje>
```

Seção sem conteúdo some. Não escreva "nada".

Grave a mesma saída em `Diario/AAAA-MM-DD.md`, na seção "Manhã", e faça commit e push.

## Regras

- No máximo 15 linhas. Detalhe só se ele pedir.
- Nunca invente compromisso, prazo ou renovação. Sem fonte, não entra.
- Termine com uma sugestão só, não uma lista.
