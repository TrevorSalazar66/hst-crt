# Protocolo: Modo Interativo (`interativo`)

> **Propósito do Modo:** Proporcionar uma **experiência imersiva de RPG Solo e Livro-Jogo**. A IA atua como Mestre e Narradora do mundo, conduzindo a história com base no estado dinâmico e nos oráculos, enquanto o **usuário assume a perspectiva do protagonista**, tomando decisões táticas e morais críticas a cada bifurcação da trama.

---

## 🎮 1. Dinâmica do Modo: Mestre & Jogador

Ao contrário do [Modo Co-Autor](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/protocolos/modo_coautor.md) (onde o usuário atua como roteirista aprovando esboços), no **Modo Interativo** o usuário joga através dos olhos do personagem:

* A cena é narrada em prosa imersiva até o **ponto de tensão máxima ou bifurcação de caminhos**.
* A narrativa **PAUSA** e apresenta opções de ação tática + campo para ação livre.
* A decisão do jogador dita o rumo do capítulo seguinte e gera custos imediatos em recursos.

---

## 🔄 2. Ciclo de Execução por Capítulo

```
[ 1. Estado & Ação Prévia ] ➔ [ 2. Rolar Oráculos ] ➔ [ 3. Redigir Cena até o Impasse ] ➔ [ 4. Apresentar Opções & PAUSA ] ➔ [ 5. Sincronizar Estado ]
```

### Passo 1: Leitura de Recursos Disponíveis e Ação Escolhida

* Verifique a escolha feita pelo jogador no turno anterior.
* Consulte `background/dinamico/estado_personagens.json` para saber exatamente quanta saúde, munição, ferramentas ou elixires o protagonista possui antes de narrar o resultado da ação.

### Passo 2: Consulta aos Oráculos

* Execute `scripts/oraculo/gerador_premissa.py` para determinar a resposta do ambiente ou a complicação do oráculo perante a ação do jogador.

### Passo 3: Redação do Capítulo (`saga/capitulo_XX.md`)

* Escreva a cena em prosa fluida e envolvente seguindo [construcao_cena.md](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/metodologias/construcao_cena.md).
* Conduza a ação até o momento em que uma decisão crucial precisa ser tomada (o *Ponto de Inflexão / Clímax Tático*).

### Passo 4: Apresentação do Menu de Decisão & PAUSA OBRIGATÓRIA 🛑

Ao final do texto, exiba o menu de escolhas no chat e **PAUSE IMEDIATAMENTE**.

---

## 📋 3. Formato Padrão do Menu de Decisão no Chat

```markdown
---

### 🛡️ Status Atual do Protagonista:
* **Condição / Saúde:** [Ex: 70% — Ferimento leve no ombro esquerdo]
* **Equipamento Crítico:** [Ex: Revólver (3 tiros restantes) | 1x Filtro de Ar | Gazua]
* **Nível de Perigo / Alerta:** [Ex: Moderado — Patrulha a 2 quarteirões]

---

### 🎲 O que você decide fazer agora?

1. **[Abordagem Direta / Confronto]:** [Descrição da ação de força ou combate e o risco evidente associado].
2. **[Abordagem Furtiva / Engenhosa]:** [Descrição da tentativa de contorno, fuga ou uso de ferramenta especializada].
3. **[Abordagem Social / Ousada]:** [Descrição de blefe, negociação arriscada ou uso do ambiente/suborno].
4. **[Ação Livre]:** *Digite exatamente o que deseja que o protagonista faça ou diga.*

👉 *Digite o número da sua escolha (1, 2, 3) ou descreva sua ação personalizada:*
```

---

## ⚖️ 4. Regras de Design de Escolhas (Princípio da Agência Real)

1. **Sem Falsas Escolhas (Sem Ilusão):** Cada uma das 3 opções deve representar uma estratégia genuinamente diferente com consequências e custos táticos distintos.
2. **Validação Rígida de Inventário:**
   * Se a Opção 2 exige arrombar uma porta com gazua e o jogador não possui gazuas em `estado_personagens.json`, essa opção **não pode** ser oferecida (ou deve vir acompanhada de um aviso de improviso com alto risco de quebra).
3. **Custos e Consequências Reais:**
   * Escolhas agressivas devem consumir munição ou arriscar dano corporal.
   * Escolhas lentas ou cautelosas devem permitir o avanço do tempo limite (*Ticking Clock*) ou alertar patrulhas.
4. **Respeito à Ação Livre do Usuário:** Se o usuário optar por uma ação fora das 3 opções sugeridas, o narrador deve honrar a criatividade do jogador, aplicando a lógica do mundo e as consequências proporcionais.

---

## 💾 5. Sincronização e Avanço de Capítulo

1. Ao receber a resposta do usuário, resolva a ação no início do capítulo seguinte (`saga/capitulo_XX.md`).
2. Atualize os JSONs de `background/dinamico/` imediatamente após registrar os gastos e ferimentos.
3. Avance o contador em `config/config_geral.json`.
