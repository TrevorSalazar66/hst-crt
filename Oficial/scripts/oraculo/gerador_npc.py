import json
import random
from pathlib import Path
from typing import Dict, Any

def sortear_de_lista(opcoes: list) -> Dict[str, Any]:
    """Realiza sorteio ponderado a partir de uma lista de opções com 'item', 'peso' e 'descricao'."""
    pesos = [op.get("peso", 1) for op in opcoes]
    escolha = random.choices(opcoes, weights=pesos, k=1)[0]
    return {
        "item": escolha.get("item"),
        "descricao": escolha.get("descricao", "")
    }

def gerar_perfil_npc(caminho_arquivo: str = "Oficial/oraculos/personalidade_npc.json") -> Dict[str, Any]:
    """Gera um perfil psicológico e comportamental completo de NPC a partir das tabelas modulares."""
    caminho = Path(caminho_arquivo)
    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    arquetipo = sortear_de_lista(dados["arquetipos"])
    traco = sortear_de_lista(dados["tracos_personalidade"])
    trejeito = sortear_de_lista(dados["trejeitos"])
    vicio = sortear_de_lista(dados["vicios"])
    fraqueza_moral = sortear_de_lista(dados["fraquezas_morais"])
    falha_fatal = sortear_de_lista(dados["falhas_fatais"])
    valor = sortear_de_lista(dados["valores"])
    crenca = sortear_de_lista(dados["crencas"])

    perfil = {
        "arquetipo": arquetipo,
        "traco_dominante": traco,
        "trejeito_marcante": trejeito,
        "vicio": vicio,
        "fraqueza_moral": fraqueza_moral,
        "falha_fatal": falha_fatal,
        "valor_fundamental": valor,
        "crenca_filosofica": crenca
    }
    return perfil

import sys
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

if __name__ == "__main__":
    caminho_base = Path(__file__).resolve().parent.parent.parent
    caminho_json = caminho_base / "oraculos" / "personalidade_npc.json"
    npc_sorteado = gerar_perfil_npc(str(caminho_json))
    print("\n==========================================")
    print("👤 PERFIL DE PERSONALIDADE DE NPC SORTEADO")
    print("==========================================")
    print(json.dumps(npc_sorteado, indent=2, ensure_ascii=False))
    print("==========================================\n")
