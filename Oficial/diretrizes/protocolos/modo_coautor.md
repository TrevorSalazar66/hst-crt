# Protocolo: Modo Co-Autor (`coautor`)

> **Propósito do Modo:** Estabelecer uma **parceria criativa dinâmica de sala de roteiro** entre o usuário e a IA. A IA atua como co-autora: propõe premissas, consulta oráculos e sugere desdobramentos dramáticos, mas o **usuário detém o controle editorial supremo**, aprovando ou refinando o esboço antes de qualquer prosa ser escrita.

---

## 🔄 1. Ciclo de Execução por Capítulo

```
[ 1. Leitura de Contexto & Estado ] ➔ [ 2. Consulta aos Oráculos ] ➔ [ 3. Proposta & PAUSA ] ➔ [ 4. Redação do Capítulo ] ➔ [ 5. Sincronização de Estado ]
```

### Passo 1: Leitura de Contexto e Estado Atual

1. Leia `config/config_geral.json` para identificar o `capitulo_atual` e o tom ativo.
2. Consulte os arquivos de estado em `background/dinamico/`:
   - `estado_mundo.json`: Tensão da região, alertas de facções e clima ambiental.
   - `estado_personagens.json`: Saúde, inventário/munição restante e atitude dos companheiros/NPCs.
   - `estado_trama.json`: *Plot hooks* ativos e urgências imediatas.
3. Consulte as regras do universo e lore fixo em `background/fixo/` pertinentes ao local atual.

### Passo 2: Execução dos Oráculos

1. Execute `scripts/oraculo/gerador_premissa.py` ou consulte as tabelas em `oraculos/`:
   - **Semente de Cena (`sementes_cena.json`):** Dinâmica e objetivo imediato.
   - **Reviravolta Prevista (`reviravoltas.json`):** Complicação ou choque para a Fase 3 da cena.
   - **Reação/Personalidade de NPC (`personalidade_npc.json`):** Atitude ou trejeito do coadjuvante envolvido.

### Passo 3: Apresentação da Proposta de Cena & PAUSA OBRIGATÓRIA 🛑

Apresente a proposta estruturada no chat e **PAUSE IMEDIATAMENTE**, sem redigir o texto da história.

#### 📋 Formato Padrão da Proposta no Chat

```markdown
### 🎲 Proposta para o Capítulo [XX]: [Sugestão de Título]

* **Foco Narrativo & Semente:** [Objetivo imediato + semente sorteada]
* **Localização & Atmosfera:** [Onde a cena se passa e elementos sensoriais dominantes]
* **Nível de Tensão Calibrado:** [Baixo / Moderado / Alto / Crítico]
* **Reviravolta em Potencial:** [Sorteio do oráculo a ser injetado no meio da cena]

#### 📝 Esboço dos 5 Blocos da Cena:
1. **Entrada (In Media Res):** [Como o capítulo começa e qual a urgência imediata]
2. **Atrito / Desenvolvimento:** [O esforço do protagonista e o obstáculo inicial]
3. **Ponto de Inflexão:** [O momento em que a reviravolta acontece ou os planos mudam]
4. **Clímax Tático:** [A ação decisiva ou escolha difícil do protagonista]
5. **Consequência & Gancho:** [O custo amargo, recursos gastos e o gancho final]

---
👉 *Deseja aprovar este esboço, alterar algum ponto ou sortear novos elementos antes da redação final?*
```

---

## ✍️ 2. Redação do Capítulo (Após Aprovação do Usuário)

Assim que o usuário responder aprovando ou solicitando ajustes específicos:

1. **Incorpore o Feedback:** Adapte o esboço conforme as instruções do usuário (ex: trocar a arma utilizada, focar em um diálogo específico ou mudar a gravidade da consequência).
2. **Escreva em Prosa Literária de Alto Impacto:**
   - Siga rigorosamente as diretrizes de [construcao_cena.md](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/metodologias/construcao_cena.md) e [ritmo_e_tensao.md](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/metodologias/ritmo_e_tensao.md).
   - Aplique *Show, Don't Tell*, ancoragem sensorial nos cinco sentidos e subtexto nos diálogos.
3. **Grave o Arquivo do Capítulo:**
   - Salve o texto completo em `saga/capitulo_XX.md` (onde `XX` é o número formatado com dois dígitos, ex: `capitulo_01.md`).
   - Inclua o cabeçalho padronizado e a seção final de **Consequências & Atualizações da Cena**.

---

## 💾 3. Sincronização do Estado Dinâmico

Após a redação do capítulo:

1. Execute `scripts/gestao/gerenciador_estado.py` ou atualize manualmente os JSONs em `background/dinamico/`:
   - **`estado_personagens.json`:** Registre danos à saúde, filtros/munição gastos e itens obtidos.
   - **`estado_trama.json`:** Avance o status dos ganchos trabalhados e adicione novas pistas/ameaças surgidas na cena.
   - **`estado_mundo.json`:** Atualize o nível de alerta do local e a reputação com facções.
2. Atualize o `capitulo_atual` em `config/config_geral.json` incrementando em `+1`.
3. Notifique o usuário com um resumo conciso das mudanças de estado e prepare-se para o próximo capítulo.

---

## ⚖️ 4. Regras Soberanas do Modo Co-Autor

1. **Proibido Gerar o Capítulo Sem Aprovação Prévia:** O agente jamais deve gerar o texto do capítulo no mesmo turno em que propõe o esboço. A pausa para validação é inviolável.
2. **O Usuário Tem Poder de Veto e Direção:** Se o usuário rejeitar uma reviravolta do oráculo ou decidir que o protagonista tomará uma atitude inesperada, a vontade do usuário prevalece sobre qualquer sorteio mecânico.
3. **Coerência Cumulativa Rígida:** Não ignore consequências de capítulos anteriores. Se o protagonista machucou a perna no Capítulo anterior, ele deve mancar e sentir dor no Capítulo atual.
