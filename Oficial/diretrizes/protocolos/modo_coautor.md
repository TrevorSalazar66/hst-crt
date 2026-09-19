# Protocolo: Modo Co-Autor (`coautor`)

No modo **Co-Autor**, o agente e o usuário escrevem juntos em um ciclo de proposta e aprovação.

## Fluxo de Trabalho:
1. O agente rola o oráculo e lê os estados dinâmicos.
2. O agente apresenta no chat:
   - 🎲 **Resultados dos Oráculos**
   - 📝 **Esboço da Cena Proposta** (3 a 5 pontos)
3. O agente **PAUSA** e aguarda o usuário aprovar, alterar ou sugerir mudanças no esboço.
4. Após o feedback do usuário, o agente gera o texto do capítulo em `saga/capitulo_XX.md`.
5. O agente roda o script de estado para atualizar os JSONs.
