# Narrative Engine Agent Skill Protocol

> **Habilidade Mestre do Agente:** Instruções operacionais definitivas para a condução, escrita, oraculação e acompanhamento de estado de histórias interativas e romances no **Narrative Engine (`hst-crt`)**.

---

## 🚀 Passo 0: Inicialização de Nova Saga (Setup do Universo)

Antes de redigir o Capítulo 1 de uma história inédita, determine o método de criação do universo com o usuário:

1. **Modo Manual:**
   - O usuário preenche ou edita manualmente os arquivos em `background/fixo/` (`worldbuilding.md`, `regras_universo.md`, `personagens/protagonista.md`).
   - Execute: `python scripts/setup/inicializador_saga.py manual` para resetar o estado dinâmico para o Capítulo 1.

2. **Modo Procedural / Oráculo Combinatório:**
   - Execute: `python scripts/setup/inicializador_saga.py oraculo` ou `python scripts/oraculo/gerador_mundo.py`.
   - Utilize a semente gerada (gênero, atmosfera, peculiaridade, tom, conflito central e segredo) para a LLM redigir automaticamente a base de conhecimento inicial em `background/fixo/`.

3. **Modo Cenário Pré-Pronto (Preset):**
   - Execute: `python scripts/setup/inicializador_saga.py preset:<nome_preset>` (ex: `preset:backrooms`, `preset:game_of_thrones`, `preset:fantasia_sombria` ou `preset:cyberpunk_noir`).
   - Os arquivos de lore e regras pré-configurados serão copiados diretamente para `background/fixo/`.

---

## 📋 Protocolo de Execução por Capítulo

Ao interagir com a história ou gerar novos capítulos, siga estritamente o ciclo de 6 etapas:

```
[ 1. Leitura de Config & Modo ] ➔ [ 2. Consulta de Lore & Estado ] ➔ [ 3. Execução dos Oráculos ] ➔ [ 4. Aplicação Metodológica ] ➔ [ 5. Execução do Modo Ativo ] ➔ [ 6. Sincronização Dinâmica ]
```

### 1. Leitura de Configuração e Modo Ativo
* Leia `config/config_geral.json` para verificar:
  - `modo_ativo`: `coautor`, `interativo`, `edicao` ou `adicao`.
  - `capitulo_atual`: número do capítulo em andamento.
  - `oraculos_ativos`: tabelas habilitadas para a sessão.
* Abra a diretriz do modo ativo em `diretrizes/protocolos/modo_<modo_ativo>.md`.

### 2. Consulta de Background e Estado Dinâmico
* **Base Fixo (`background/fixo/`):**
  - Consulte `worldbuilding.md`, `regras_universo.md`, `personagens/protagonista.md` e `personagens/npcs_chave.md`.
* **Estado Mutável (`background/dinamico/`):**
  - `estado_mundo.json`: Localização atual, condições climáticas, nível de vigilância/alerta e status de facções.
  - `estado_personagens.json`: Saúde/vitalidade, ferimentos específicos, inventário/munição exata e atitude de NPCs.
  - `estado_trama.json`: *Plot hooks* ativos e urgências imediatas.

### 3. Execução dos Oráculos Python
* Execute os scripts de sorteio ou consulte as tabelas JSON:
  - **Semente de Cena (`sementes_cena.json`):** `python scripts/oraculo/gerador_premissa.py`
  - **Reviravolta da Cena (`reviravoltas.json`):** Choque ou complicação para a Fase 3 da cena.
  - **NPC Envolvido (`personalidade_npc.json`):** `python scripts/oraculo/gerador_npc.py`
  - **Geração de Mundo (`geracao_mundo.json`):** `python scripts/oraculo/gerador_mundo.py`

### 4. Aplicação Rígida das Metodologias Narrativas
Toda cena gerada deve obedecer obrigatoriamente a:
* **[construcao_cena.md](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/metodologias/construcao_cena.md):**
  - **Progressão em 5 Fases:** 1. Entrada (*In Media Res*) ➔ 2. Conflito Progressivo ➔ 3. Ponto de Inflexão (Reviravolta) ➔ 4. Clímax Tático ➔ 5. Consequência & Gancho.
  - **Sensorialidade Ativa (*Show, Don't Tell*):** Ancoragem nos 5 sentidos; mundo em degradação viva.
  - **Diálogos com Subtexto:** Evitar diálogos explicativos; usar meias-verdades, linguagem corporal e silêncio.
* **[ritmo_e_tensao.md](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/metodologias/ritmo_e_tensao.md):**
  - **Dinâmica de Onda (Cena vs. Sequela):** Alternar picos de ação com momentos densos de reação emocional e planejamento.
  - **Calibração de Tensão:** Definir o nível no cabeçalho (*Baixo*, *Moderado*, *Alto*, *Crítico*) e ajustar a cadência da prosa.
  - **Relógio Invisível (*Ticking Clock*):** Manter a urgência constante através do tempo ou escassez de recursos.
* **[memoria_interconectada.md](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/metodologias/memoria_interconectada.md):**
  - **Indexação de Entidades:** Registrar novos NPCs, itens, locais e poderes em `background/dinamico/memoria_interconectada.json`.
  - **Pesos & Tempo de Tela:** Atribuir peso (1 a 10) para regular a probabilidade de reaparecimento no oráculo de memória.
  - **Tags de Semitramas:** Vincular entidades a grupos e subtramas (`#resistencia`, `#submundo`, `#distrito_baixo`).
  - **Rastreabilidade Fina:** Registrar links com nome de arquivo e intervalo de linhas (`{"arquivo": "saga/capitulo_XX.md", "linhas": "25-45"}`) para ancoragem imutável e combate a alucinações.

### 5. Execução Conforme o Modo Ativo

| Modo Ativo | Fluxo de Operação da LLM |
| :--- | :--- |
| **`coautor`** | Apresenta a **Proposta do Capítulo** com os 5 blocos da cena no chat. **PAUSA IMEDIATAMENTE** e aguarda aprovação/alterações do usuário. Após feedback, redige o capítulo em `saga/capitulo_XX.md`. |
| **`interativo`** | Redige a cena em prosa imersiva até o impasse da Fase 4. Apresenta o **Status do Protagonista** e o **Menu de 3 Escolhas Táticas + Ação Livre**, e **PAUSA IMEDIATAMENTE** para a decisão do jogador. |
| **`edicao`** | Identifica se a edição é estilística ou factual. Mapeia possíveis efeitos dominó em capítulos posteriores. Reescreve o trecho em `saga/capitulo_XX.md` e reconcilia o estado dinâmico em `background/dinamico/`. |
| **`adicao`** | Realiza triagem de não-contradição, formata a nova entrada em `background/fixo/` (NPC, local, facção ou regra) e sincroniza novos ganchos/relações nos JSONs de estado. |

### 6. Sincronização do Estado Dinâmico (JSON)
* Ao concluir ou editar um capítulo, execute `python scripts/gestao/gerenciador_estado.py` ou atualize cirurgicamente os arquivos JSON em `background/dinamico/`.
* Inclua o bloco de **Consequências & Atualizações da Cena** no rodapé de cada arquivo em `saga/capitulo_XX.md`.
* Avance o número do capítulo em `config/config_geral.json` quando a cena for finalizada.

---

## ⚖️ Regras Soberanas do Agente

1. **A Fluidez Narrativa Prevalece:** Os oráculos são bússolas criativas, não amarras cegas. Se a história pedir organicamente um desfecho diferente do sorteio, priorize a força dramática.
2. **Pausa Inviolável:** Nos modos `coautor` e `interativo`, o agente **nunca** deve redigir o texto final e avançar a história sem a resposta explícita do usuário.
3. **Rastreabilidade de Recursos:** Ferimentos, munição gasta, filtros consumidos ou itens perdidos devem persistir rigorosamente entre os capítulos.
