# Metodologia de Construção de Cena e Diretrizes Narrativas

> **Princípio Soberano:** A prioridade absoluta é sempre a **fluidez dramática, a consistência lógica e a excelência narrativa**. As tabelas de oráculo servem como ferramentas de inspiração e catalisadores criativos, e **não** como amarras mecânicas obrigatórias. Se a trama orgânica ou a escolha do usuário pedir um rumo diferente de um sorteio, a narrativa deve prevalecer.

---

## 🖋️ 1. Boas Práticas de Escrita e Estilo

### Sensorialidade e Ambientação (*Show, Don't Tell*)

* **Ancoragem nos Sentidos:** Nunca descreva uma sala apenas visualmente. Traga o cheiro da fuligem úmida, o estalo do metal sob pressão de vapor, a textura oleosa da chuva ácida ou o peso da máscara de chumbo sobre a pele.
* **Mundo em Degradação Ativa:** O maquinário range, as lâmpadas a gás piscam, os filtros de ar assobiam e as roupas estão desgastadas. Evite elementos com aparência de "novos em folha" a menos que pertençam aos barões do Consórcio.

### Diálogos Vivos e Subtexto

* **Evite o Óbvio:** Personagens não devem verbalizar abertamente todos os seus sentimentos ou expor planos inteiros em voz alta. Use meias-verdades, silêncios calculados e ironia.
* **Linguagem Não-Verbal e Gestual:** Lembre-se do impacto do Silêncio e linguagem não verbal. Movimentos curtos de cabeça, desvio de olhar e toques em armas ou amuletos comunicam tanto quanto palavras.

### Ritmo e Economia de Recursos

* **Peso das Consequências:** Cada tiro disparado, dose de elixir consumida ou filtro de ar gasto deve ter peso dramático e ser registrado no estado do inventário.
* **Equilíbrio de Frases:** Em momentos de perigo ou ação rápida, use frases mais curtas e verbos de impacto. Em momentos de investigação ou reflexão, use parágrafos mais densos e reflexivos.

---

## 📄 2. Formatação Padrão do Capítulo

Para manter a consistência em todos os arquivos de saga (`saga/capitulo_XX.md`), adote o seguinte padrão:

```markdown
# Capítulo [XX]: [Título Evocativo do Capítulo]

> **Foco Narrativo:** [Semente do oráculo ou objetivo principal do capítulo]  
> **Localização:** [Local e distrito em que a cena acontece]  
> **Estado de Tensão:** [Baixo / Moderado / Alto / Crítico]

---

[Texto da cena em prosa fluida, dividido em parágrafos bem espaçados...]

> *"Diálogos em linguagem de sinais ou sussurros podem ser formatados assim para reforçar a ambientação de sigilo."* Por exemplo.

---

### 📌 Consequências & Atualizações da Cena
* **Saúde & Condição:** [Danos sofridos, fadiga, exposição à névoa]
* **Recursos & Inventário:** [Filtros gastos, munição, itens adquiridos]
* **Ganchos & Segredos:** [Novas perguntas ou pistas abertas para o próximo capítulo]
```

---

## 🎭 3. Guia das 5 Fases Dramáticas da Cena

Cada capítulo deve ser construído seguindo uma progressão em cinco etapas bem articuladas:

```
[1. Entrada / Ancoragem] ➔ [2. Atrito / Desenvolvimento] ➔ [3. Ponto de Inflexão] ➔ [4. Clímax Tático] ➔ [5. Consequência / Gancho]
```

### Fase 1: Entrada e Ancoragem (*In Media Res*)

* **Objetivo:** Estabelecer imediatamente onde o personagem está, o que ele precisa resolver agora (o *Objetivo Imediato*) e qual é o fator de urgência (contagem regressiva, patrulha se aproximando, filtro acabando).
* **Execução:** Inicie próximo ao momento da ação ou logo após um gatilho inicial, sem enrolações expositivas longas.

### Fase 2: Conflito Progressivo e Atrito

* **Objetivo:** O protagonista tenta executar o plano, mas encontra resistência ativa (uma tranca emperrada, a desconfiança de um guarda, a hostilidade do terreno ou uma contradição de pistas).
* **Execução:** Mostre a competência do protagonista, mas faça o mundo cobrar um preço ou esforço proporcional.

### Fase 3: Ponto de Inflexão (Onde Entra a Reviravolta)

* **Objetivo:** O momento em que o plano inicial é desafiado ou quebrado por uma nova complicação (a *Reviravolta do Oráculo* ou uma revelação chocante).
* **Execução:** O personagem percebe que a situação é mais perigosa, urgente ou moralmente cinzenta do que parecia.

### Fase 4: Clímax Tático da Cena

* **Objetivo:** A resposta ativa do protagonista perante a complicação. Uma decisão difícil, um disparo decisivo, uma mentira arriscada ou uma fuga no último segundo.
* **Execução:** Ritmo acelerado, foco nas ações físicas e no risco imediato de perda.

### Fase 5: Consequência, Custo e Gancho (*Cliffhanger*)

* **Objetivo:** A cena encerra com uma vitória parcial com custo amargo, um ferimento, um recurso gasto e uma pergunta urgente deixada no ar.
* **Execução:** Nunca termine uma cena em estabilidade absoluta. O final de um capítulo deve sempre convidar o leitor a querer saber o que acontece no minuto seguinte.

---

## 🎲 4. Função dos Oráculos e Gatilhos de Utilização

As tabelas de oráculos são ferramentas de suporte para desbloquear a criatividade e introduzir o elemento surpresa. Utilize-as conforme a necessidade da cena:

| Oráculo | Função Principal | Quando Consultar (Gatilhos Sugeridos) |
| :--- | :--- | :--- |
| **[geracao_mundo.json](hrt-crt/Oficial/oraculos/geracao_mundo.json)** | Estabelece os pilares do cenário (Gênero, Atmosfera, Poder, Governo, Peculiaridade, Ápice e Antagonista). | **Início de Saga** ou quando a história alcançar uma região inexplorada do mapa que necessita de regras próprias. |
| **[sementes_cena.json](hrt-crt/Oficial/oraculos/sementes_cena.json)** | Define a dinâmica central, o objetivo imediato e o fator de urgência do capítulo. | **Início de cada novo capítulo** para sortear o gancho ou desbloquear ideias de conflito. |
| **[reviravoltas.json](hrt-crt/Oficial/oraculos/reviravoltas.json)** | Introduz complicações inesperadas (revelações, terceiras facções, falhas de equipamento, anomalias). | **No meio da cena (Fase 3)** quando a ação estiver fluindo fácil demais ou o capítulo necessitar de um choque de tensão. |
| **[personalidade_npc.json](hrt-crt/Oficial/oraculos/personalidade_npc.json)** | Gera arquétipos, trejeitos, vícios, fraquezas morais, falhas fatais, valores e crenças de personagens secundários. | **Sempre que um novo NPC relevante entrar em cena**, ou quando for necessário aprofundar a psicologia de um coadjuvante. |

---

## ⚖️ 5. Regra da Prioridade Narrativa

1. **O Oráculo Propõe, a Trama Dispõe:** Se o oráculo sortear uma reviravolta ambiental (ex: *vazamento de vapor*), mas a cena pedir organicamente uma revelação dramática de traição entre dois irmãos, **priorize a revelação dramática**.
2. **Coerência Cumulativa:** Respeite o que foi estabelecido nos capítulos anteriores. Um NPC sorteado com honra rígida não deve trair sem uma pressão moral proporcional à sua falha fatal.
3. **Consistência de Estado:** Toda alteração de inventário, saúde ou lealdade ocorrida durante as fases da cena deve ser refletida nos arquivos de `background/dinamico/`.
