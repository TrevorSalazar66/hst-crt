# Metodologia de Memória Modular Interconectada & Rastreabilidade Fina

> **Princípio Central:** Para evitar alucinações, inconsistências de continuidade e o esquecimento de personagens ou itens ao longo de múltiplos capítulos, toda entidade relevante criada organicamente na história deve ser **indexada, categorizada por tags de semitramas, ponderada por pesos de tempo de tela e vinculada às linhas exatas dos arquivos onde aparece**.

---

## 🕸️ 1. A Estrutura da Memória Interconectada (`memoria_interconectada.json`)

Toda entidade no universo narrativo é registrada com os seguintes atributos essenciais:

```json
{
  "id": "npc_viktor_ferreiro",
  "nome": "Viktor, o Ferreiro Caolho",
  "tipo": "personagem",
  "peso": 6,
  "status": "ativo",
  "tags": ["submundo", "resistencia", "distrito_baixo", "forja"],
  "descricao": "Ferreiro veterano que perdeu o olho esquerdo. Forja armas clandestinas e conhece as rotas de fuga.",
  "aparicoes": [
    {
      "arquivo": "saga/capitulo_01.md",
      "linhas": "25-48",
      "contexto": "Primeiro encontro; consertou a faca de caça e revelou rota de fuga"
    },
    {
      "arquivo": "saga/capitulo_03.md",
      "linhas": "14-22",
      "contexto": "Entregou a chave das comportas sob pressão de patrulha"
    }
  ],
  "conexoes": [
    {
      "entidade_id": "item_faca_caca",
      "relacao": "Forjou a lâmina"
    }
  ]
}
```

---

## ⚖️ 2. Sistema de Pesos & Tempo de Tela

Os pesos numéricos regulam a probabilidade de uma entidade reaparecer nas cenas através de sorteios do oráculo de memória:

| Faixa de Peso | Categoria de Relevância | Frequência de Tempo de Tela | Exemplos |
| :--- | :--- | :--- | :--- |
| **8 a 10** | **Núcleo Central / Primário** | Quase todo capítulo ou presente no arco principal. | Aliado principal, antagonista do arco, item de assinatura do protagonista. |
| **5 a 7** | **Coadjuvante Recorrente / Secundário** | Reaparece a cada 2–4 capítulos conforme a subtrama avança. | Contato do submundo, capitão de patrulha local, esconderijo seguro. |
| **2 a 4** | **Elemento Circunstancial / Terciário** | Aparições pontuais em distritos específicos. | Mercador ocasional, informante assustado, ferramenta de uso único. |
| **1** | **Figurante / Detalhe Atmosférico** | Raramente sorteado a menos que o contexto exija. | Taberneiro rabugento, mendigo que viu uma pista. |

> 💡 **Ajuste Dinâmico:** Se um NPC secundário toma uma decisão heroica ou se torna crucial para a trama, seu peso é aumentado no arquivo para que a IA o inclua com maior frequência. Se um item é perdido ou um NPC morre, seu status muda para `"destruido_ou_morto"` ou seu peso é reduzido.

---

## 🏷️ 3. Organização por Tags & Semitramas (Subtramas)

As tags funcionam como fios condutores temáticos para agrupar entidades correlatas. Quando uma cena se passa em um contexto específico, a IA consulta entidades que compartilham essas tags:

* **Tags de Região/Distrito:** `#distrito_baixo`, `#torres_altas`, `#subsolo`, `#docas`.
* **Tags de Facção/Poder:** `#consorcio`, `#sindicato_livre`, `#culto_da_nevoa`.
* **Tags de Subtrama (Semitramas):** `#arco_vinganca`, `#cura_da_toxina`, `#golpe_ao_banco`, `#resistencia`.
* **Tags de Tipo & Combate:** `#arma_branca`, `#implante`, `#alquimia`, `#segredo_revelado`.

---

## 🔗 4. Protocolo de Rastreabilidade Fina (Links de Linhas & Arquivos)

Sempre que um novo capítulo for redigido em `saga/capitulo_XX.md`:

1. **Ao criar um elemento novo:**
   - Adicione a entidade em `background/dinamico/memoria_interconectada.json`.
   - Registre o link inicial: `{"arquivo": "saga/capitulo_XX.md", "linhas": "L15-L35", "contexto": "..."}`.
2. **Ao reintroduzir um elemento existente:**
   - Adicione uma nova entrada na lista de `aparicoes` da entidade existente, indicando o arquivo do capítulo e as linhas onde ele interagiu.
3. **Prevenção de Alucinação:**
   - Ao consultar uma entidade, leia as linhas exatas das suas aparições anteriores para garantir coerência de personalidade, itens em posse, cicatrizes e atitudes prévias.

---

## 🎲 5. Oráculo de Memória Dinâmica (`scripts/gestao/gerenciador_memoria_interconectada.py`)

Em momentos de geração de cena (Fase 1 e Fase 3):
* Execute ou simule o sorteio ponderado de entidades por tag:
  ```bash
  python scripts/gestao/gerenciador_memoria_interconectada.py
  ```
* Isso permite resgatar NPCs, itens esquecidos no inventário ou cenários familiares com base no peso de relevância de cada um, enriquecendo o senso de mundo vivo e coeso.
