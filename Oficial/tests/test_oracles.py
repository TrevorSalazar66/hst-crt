import pytest
import sys
from pathlib import Path

# Adiciona scripts/oraculo ao sys.path para importação nos testes
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir / "scripts" / "oraculo"))

from sorteador_peso import SorteadorOraculo
from gerador_premissa import gerar_premissa_capitulo

def test_sorteio_item_valido():
    pasta_oraculos = root_dir / "oraculos"
    sorteador = SorteadorOraculo(str(pasta_oraculos))
    res = sorteador.sortear_item("sementes_cena.json")
    
    assert "item" in res
    assert "tabela" in res
    assert res["item"] is not None

def test_gerador_premissa_completo():
    pasta_oraculos = root_dir / "oraculos"
    premissa = gerar_premissa_capitulo(str(pasta_oraculos))
    
    assert "foco_cena" in premissa
    assert "reviravolta" in premissa
    assert "atitude_npc" in premissa
