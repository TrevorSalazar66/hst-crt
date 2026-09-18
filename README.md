# Narrative Engine (`hst-crt`)

Gerador e co-autor de histórias narrativas orientadas a metodologias, oráculos de sorteio por peso (Python) e acompanhamento de estado mutável (JSON).

## 📌 Visão Geral

O **Narrative Engine** é um sistema modular que combina:
- **Oráculos Python**: Lógica determinística de sorteio por peso para reviravoltas, focos de cena e reações de NPCs.
- **Estado Dinâmico em JSON**: "Save game" da história rastreando saúde, inventário, relacionamentos e ganchos de enredo.
- **Lore Fixo em Markdown**: Base imutável de conhecimento sobre o cenário, magia/tecnologia e personagens.
- **Diretrizes e Skills (`skill.md`)**: Instruções mestre para orientar a LLM em cada capítulo.
- **Modos de Operação**: `coautor`, `interativo`, `edição`, `adição`.

---

## 📂 Estrutura do Repositório

```
~/ (hst-crt)
├── background/
│   ├── fixo/                  # Lore, worldbuilding e fichas dos personagens (.md)
│   └── dinamico/              # Estado mutável por capítulo (.json)
├── diretrizes/                # SKILL.md, metodologias narrativas e protocolos de modo
├── oraculos/                  # Tabelas de sorteio ponderado (.json)
├── saga/                      # Capítulos gerados (.md) e resumos
├── scripts/                   # Automações Python (gestão, oráculo, utilitários)
├── config/                    # Configurações gerais da engine
└── tests/                     # Testes unitários automatizados (pytest)
```

---

## 🚀 Como Usar

### 1. Requisitos
- Python 3.10+
- Dependências listadas em `requirements.txt`

### 2. Instalação
```bash
pip install -r requirements.txt
```

### 3. Rodar Testes de Oráculo e Estado
```bash
pytest
```

### 4. Rodar Sorteio de Oráculo pelo Terminal
```bash
python scripts/oraculo/gerador_premissa.py
```

### 5. Verificar Estado Atual
```bash
python scripts/gestao/gerenciador_estado.py --status
```
