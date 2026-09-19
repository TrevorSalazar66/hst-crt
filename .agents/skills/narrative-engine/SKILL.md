---
name: narrative-engine
description: Protocolo de geração e co-criação de histórias usando Oráculos Python, Estado JSON e Modos Narrativos.
---

# Narrative Engine Agent Skill Protocol

> Este arquivo é o espelho da habilidade em `diretrizes/skill.md`.

## 🚀 Passo 0: Inicialização de Nova Saga (Bloco 1)
Antes de iniciar o Capítulo 1 de uma história nova, determine o método de criação do universo com o usuário:
1. **Modo Manual**: O usuário preenche os arquivos em `background/fixo/` (`worldbuilding.md`, `regras_universo.md`, `protagonista.md`).
2. **Modo Semi-Aleatório (Oráculo)**: Execute `python3 scripts/setup/inicializador_saga.py oraculo`. Use o resultado sorteado para a LLM redigir automaticamente a lore e a ficha do personagem em `background/fixo/`.
3. **Modo Cenário Pré-Pronto (Preset)**: Execute `python3 scripts/setup/inicializador_saga.py preset:<nome_preset>` (ex: `fantasia_sombria` ou `cyberpunk_noir`).

---

## 📋 Protocolo de Execução por Capítulo

Ao gerar ou interagir com a história neste repositório, siga estritamente o ciclo de vida abaixo:

### Passo 1: Leitura da Configuração e Modo Ativo
1. Leia o arquivo `config/config_geral.json` para verificar o `modo_ativo` (`coautor`, `interativo`, `edição`, `adição`) e o `capitulo_atual`.
2. Abra a diretriz correspondente ao modo em `diretrizes/protocolos/modo_<modo_ativo>.md`.

### Passo 2: Consulta de Background e Estado Dinâmico
1. Leia `background/fixo/worldbuilding.md`, `regras_universo.md` e a ficha do protagonista para manter el tom e a coerência do lore.
2. Leia os arquivos de estado mutável em `background/dinamico/`:
   - `estado_mundo.json`
   - `estado_personagens.json`
   - `estado_trama.json`

### Passo 3: Execução do Oráculo Python
1. Execute o script `scripts/oraculo/gerador_premissa.py` via linha de comando ou simule o sorteio ponderado das tabelas em `oraculos/`.
2. Anote os resultados do oráculo (Semente de Cena, Reviravolta, Reação de NPC).

### Passo 4: Execução conforme o Modo Ativo
- **Modo `coautor`**:
  - Apresente primeiro os resultados do oráculo e um **esboço de 3 tópicos da cena**.
  - **PAUSE** e aguarde a aprovação ou edições do usuário no chat.
  - Após aprovação, escreva o capítulo em `saga/capitulo_XX.md`.
- **Modo `interativo`**:
  - Escreva a primeira parte da cena até o ponto de decisão.
  - Ofereça 3 opções de escolha (ou espaço para ação livre do usuário) e **PAUSE**.
- **Modo `edição`**:
  - Aplique os pedidos de alteração no capítulo especificado pelo usuário sem quebrar o estado JSON.
- **Modo `adição`**:
  - Integre novos elementos de lore em `background/fixo/` e reflita as mudanças no estado.

### Passo 5: Atualização do Estado Dinâmico (JSON)
1. Ao concluir o capítulo, execute o script Python `scripts/gestao/gerenciador_estado.py` para registrar a evolução de saúde, inventário, ganchos e avanço do número do capítulo.
