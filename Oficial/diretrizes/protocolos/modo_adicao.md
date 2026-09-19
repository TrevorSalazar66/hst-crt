# Protocolo: Modo Adição (`adicao`)

> **Propósito do Modo:** Permitir a **expansão modular e segura do universo narrativo** (worldbuilding, personagens, locais, facções, tecnologia/magia e ganchos) a qualquer momento da saga, sem alterar o capítulo em andamento e garantindo a total consistência entre a base de conhecimento e os arquivos de estado.

---

## 🎯 1. Escopo de Aplicação

O **Modo Adição** deve ser ativado quando o usuário ou o agente necessitarem:

1. Cadastrar um **novo NPC** (aliado, informante, mercador, antagonista secundário).
2. Adicionar uma **nova localização** (distrito, esconderijo, ruína, edifício corporativo).
3. Expandir as **regras do universo** (novo artefato, implante cibernético, ordem mágica, toxina ambiental).
4. Criar uma **nova facção ou sindicato** com suas metas e relações de poder.
5. Inserir **fatos históricos ou segredos pregressos** que impactem a trama futura.

---

## 🔄 2. Ciclo de Execução Passo a Passo

```
[ 1. Triagem & Não-Contradição ] ➔ [ 2. Redação Padronizada ] ➔ [ 3. Inserção no Lore Fixo ] ➔ [ 4. Sincronização Dinâmica ] ➔ [ 5. Confirmação ]
```

### Passo 1: Análise de Não-Contradição

* Antes de registrar qualquer elemento, consulte `background/fixo/` e os capítulos já escritos em `saga/`.
* **Regra de Ouro:** O novo elemento não pode quebrar a lógica ou anular fatos já testemunhados pelo leitor, a menos que seja explicitamente introduzido como *mentira desmascarada* ou *revelação de bastidores*.

### Passo 2: Roteamento de Arquivos

Direcione cada tipo de informação para o seu destino correto em `background/fixo/`:

| Tipo de Adição | Arquivo de Destino | Seção Recomendada |
| :--- | :--- | :--- |
| **NPC / Personagem Secundário** | `background/fixo/personagens/npcs_chave.md` | Nova seção `### [Nome do NPC]` com ficha padrão. |
| **Distrito / Localidade / Ponto de Interesse** | `background/fixo/worldbuilding.md` | Sob `## Geografia, Distritos e Locais`. |
| **Regra de Magia / Tecnologia / Biologia** | `background/fixo/regras_universo.md` | Sob `## Sistemas de Poder / Tecnologia`. |
| **Facção / Sindicato / Corporação** | `background/fixo/worldbuilding.md` | Sob `## Facções, Governos e Poder`. |
| **Protagonista (Novo Traço/Habilidade)** | `background/fixo/personagens/protagonista.md` | Sob `## Habilidades e Equipamentos`. |

### Passo 3: Sincronização com o Estado Dinâmico (`background/dinamico/`)

Toda adição que possa gerar consequências imediatas nas próximas cenas deve ser refletida nos JSONs:

* **Novo NPC com lealdade/atitude:** Registrar em `estado_personagens.json` com nível de relacionamento inicial, localização e estado de saúde.
* **Nova oportunidade ou ameaça:** Inserir um novo *plot hook* ativo em `estado_trama.json` (com status `"ativo"` e prioridade correspondente).
* **Mudança no equilíbrio de poder ou alerta regional:** Atualizar a tensão do distrito ou nível de vigilância em `estado_mundo.json`.

### Passo 4: Confirmação e Síntese

Apresente ao usuário uma resposta estruturada contendo:

* **Resumo do elemento adicionado.**
* **Arquivos modificados** (com links).
* **Potenciais ganchos** que este elemento abriu para os próximos capítulos.

---

## 📋 3. Templates Padrão de Inserção

### A) Template: Ficha de NPC (`npcs_chave.md`)

```markdown
### [Nome do NPC] — *[Alcunha ou Cargo]*
* **Arquétipo & Ocupação:** [Ex: Mercador do mercado negro / Soldado desertor]
* **Aparência Marcante:** [Traço visual imediato: cicatriz, tique, vestimenta gasta]
* **Motivação Central:** [O que o move: dinheiro, vingança, sobrevivência familiar]
* **Fraqueza Moral / Falha Fatal:** [Ex: Ganância cega, vício em elixir, lealdade ingênua]
* **Afiliação:** [Facção ou neutro] | **Atitude Inicial:** [Hostil / Desconfiado / Neutro / Amigável]
* **Segredo / Gancho Oculto:** [Informação que ele esconde do protagonista]
```

### B) Template: Ponto de Interesse / Local (`worldbuilding.md`)

```markdown
### [Nome do Local] — *[Tipo: Distrito / Ruína / Estabelecimento]*
* **Atmosfera & Sensações:** [Cheiros, iluminação, ruídos característicos]
* **Perigo / Ameaça Dominante:** [Patrulhas do Consórcio, névoa densa, radiação, ladrões]
* **Facção Controladora:** [Quem dita as ordens no local]
* **Utilidade Tática:** [Ponto de recarga de suprimentos, rota de fuga, mercado clandestino]
```

### C) Template: Relíquia / Tecnologia / Magia (`regras_universo.md`)

```markdown
### [Nome do Item / Fenômeno]
* **Natureza & Origem:** [Artefato ancestral / Protótipo a vapor / Mutação orgânica]
* **Efeito Primário:** [O que faz concretamente quando ativado]
* **Custo & Limitações:** [Consumo de combustível, fadiga mental, desgaste de peças]
* **Risco de Colapso / Efeito Colateral:** [O que acontece se for usado em excesso ou danificado]
```

---

## ⚖️ 4. Regras de Integridade do Modo

1. **Imutabilidade do Capítulo:** O Modo Adição **nunca** avança o `capitulo_atual` em `config/config_geral.json` nem redige texto em `saga/`.
2. **Economia de Informação:** Evite criar detalhes irrelevantes que sobrecarreguem o contexto da LLM. Foque em elementos que gerem atrito dramático, escolhas ou opções táticas.
3. **Persistência de Dados:** Nunca substitua arquivos inteiros; sempre anexe (*append*) ou integre cirurgicamente o novo conteúdo nas seções pertinentes.
