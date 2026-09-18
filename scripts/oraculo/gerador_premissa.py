import json
from pathlib import Path
from typing import Dict, Any
from sorteador_peso import SorteadorOraculo

def gerar_premissa_capitulo(pasta_oraculos: str = "oraculos") -> Dict[str, Any]:
    """Combina sorteios das tabelas ativas para gerar a semente completa de um capítulo."""
    sorteador = SorteadorOraculo(pasta_oraculos=pasta_oraculos)
    
    semente_cena = sorteador.sortear_item("sementes_cena.json")
    reviravolta = sorteador.sortear_item("reviravoltas.json")
    reacao_npc = sorteador.sortear_item("reacoes_npc.json")
    
    premissa = {
        "foco_cena": semente_cena["item"],
        "foco_descricao": semente_cena["descricao"],
        "reviravolta": reviravolta["item"],
        "reviravolta_descricao": reviravolta["descricao"],
        "atitude_npc": reacao_npc["item"],
        "atitude_npc_descricao": reacao_npc["descricao"]
    }
    return premissa

if __name__ == "__main__":
    caminho_script = Path(__file__).parent
    pasta_oraculos = caminho_script.parent.parent / "oraculos"
    resultado = gerar_premissa_capitulo(str(pasta_oraculos))
    print("\n==========================================")
    print("🎲 SEMENTE NARRATIVA SORTEADA PELO ORÁCULO")
    print("==========================================")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    print("==========================================\n")
