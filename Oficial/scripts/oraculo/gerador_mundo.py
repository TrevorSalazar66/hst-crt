import json
import random
from pathlib import Path
from typing import Dict, Any

def sortear_de_lista(opcoes: list) -> str:
    """Realiza sorteio ponderado a partir de uma lista de dicionários com 'item' e 'peso'."""
    itens = [op["item"] for op in opcoes]
    pesos = [op.get("peso", 1) for op in opcoes]
    return random.choices(itens, weights=pesos, k=1)[0]

def gerar_mundo(caminho_arquivo: str = "oraculos/geracao_mundo.json") -> Dict[str, Any]:
    caminho = Path(caminho_arquivo)
    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    genero = sortear_de_lista(dados["generos"])
    atmosfera = sortear_de_lista(dados["adjetivos_atmosfera"])
    sistema_poder_nivel = sortear_de_lista(dados["sistema_poder_nivel"])
    
    # Se o nível de poder for "Nenhum", a fonte pode ser indicada como Inexistente / Não aplicável
    if "Nenhum" in sistema_poder_nivel:
        sistema_poder_fonte = "Não aplicável (Mundo puramente mundano/tecnologia convencional)"
    else:
        sistema_poder_fonte = sortear_de_lista(dados["sistema_poder_fonte"])

    sistema_governo = sortear_de_lista(dados["sistemas_governo"])
    
    # Peculiaridade modular em 3 partes
    pec_condicao = sortear_de_lista(dados["peculiaridades_condicoes"])
    pec_manifestacao = sortear_de_lista(dados["peculiaridades_manifestacoes"])
    pec_impacto = sortear_de_lista(dados["peculiaridades_impactos_sociais"])
    peculiaridade_completa = f"{pec_condicao}, {pec_manifestacao}, {pec_impacto}."

    tom_mundo = sortear_de_lista(dados["tons_mundo"])
    tom_narrativa = sortear_de_lista(dados["tons_narrativa"])
    apice = sortear_de_lista(dados["apice_cenario"])
    antagonista_tipo = sortear_de_lista(dados["antagonistas_tipo"])
    antagonista_motivacao = sortear_de_lista(dados["antagonistas_motivacao"])

    mundo_sorteado = {
        "genero": genero,
        "atmosfera": atmosfera,
        "sistema_poder": {
            "nivel": sistema_poder_nivel,
            "fonte": sistema_poder_fonte
        },
        "sistema_governo": sistema_governo,
        "peculiaridade_modular": {
            "condicao": pec_condicao,
            "manifestacao": pec_manifestacao,
            "impacto_social": pec_impacto,
            "frase_completa": peculiaridade_completa
        },
        "tom_mundo": tom_mundo,
        "tom_narrativa": tom_narrativa,
        "apice_cenario": apice,
        "antagonista": {
            "tipo": antagonista_tipo,
            "motivacao": antagonista_motivacao
        }
    }
    return mundo_sorteado

if __name__ == "__main__":
    caminho_base = Path(__file__).resolve().parent.parent.parent
    caminho_json = caminho_base / "oraculos" / "geracao_mundo.json"
    resultado = gerar_mundo(str(caminho_json))
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
