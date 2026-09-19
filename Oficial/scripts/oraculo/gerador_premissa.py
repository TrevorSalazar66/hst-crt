import json
import sys
from pathlib import Path
from typing import Dict, Any
from sorteador_peso import SorteadorOraculo

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def gerar_premissa_capitulo(pasta_oraculos: str = "Oficial/oraculos") -> Dict[str, Any]:
    """Combina sorteios modulares de cena, reviravolta e NPC para gerar a semente completa de um capítulo."""
    sorteador = SorteadorOraculo(pasta_oraculos=pasta_oraculos)
    
    semente_cena = sorteador.sortear_semente_cena()
    reviravolta = sorteador.sortear_reviravolta()
    
    # Sorteio de perfil de NPC a partir de personalidade_npc.json
    dados_npc = sorteador.carregar_tabela("personalidade_npc.json")
    arquetipo_npc = sorteador.sortear_de_lista(dados_npc.get("arquetipos", []))
    traco_npc = sorteador.sortear_de_lista(dados_npc.get("tracos_personalidade", []))
    trejeito_npc = sorteador.sortear_de_lista(dados_npc.get("trejeitos", []))
    vicio_npc = sorteador.sortear_de_lista(dados_npc.get("vicios", []))
    fraqueza_npc = sorteador.sortear_de_lista(dados_npc.get("fraquezas_morais", []))
    
    premissa = {
        "cena": semente_cena,
        "reviravolta": reviravolta,
        "npc_em_destaque": {
            "arquetipo": arquetipo_npc["item"],
            "traco": traco_npc["item"],
            "trejeito": trejeito_npc["item"],
            "vicio": vicio_npc["item"],
            "fraqueza_moral": fraqueza_npc["item"]
        }
    }
    return premissa

if __name__ == "__main__":
    caminho_script = Path(__file__).resolve().parent
    pasta_oraculos = caminho_script.parent.parent / "oraculos"
    resultado = gerar_premissa_capitulo(str(pasta_oraculos))
    print("\n=======================================================")
    print("🎲 SEMENTE NARRATIVA MODULAR DO CAPÍTULO (ORÁCULO)")
    print("=======================================================")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    print("=======================================================\n")
