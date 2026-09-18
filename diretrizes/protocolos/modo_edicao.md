# Protocolo: Modo Edição (`edicao`)

Utilizado para ajustar capítulos já gerados.

## Fluxo de Trabalho:
1. O usuário indica qual capítulo deseja modificar e o que deseja alterar (ex: "No Capítulo 2, faça o diálogo mais tenso e adicione um ferimento no braço do protagonista").
2. O agente reescreve o arquivo `saga/capitulo_XX.md`.
3. O agente executa `scripts/gestao/gerenciador_estado.py` para refletir as alterações no estado JSON (ex: adicionar o ferimento em `estado_personagens.json`).
