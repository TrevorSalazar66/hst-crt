import pytest
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir / "scripts" / "gestao"))

from gerenciador_estado import GerenciadorEstado
from validador_schema import validar_integridade_schemas

def test_validacao_schemas():
    pasta_dinamico = root_dir / "background" / "dinamico"
    assert validar_integridade_schemas(str(pasta_dinamico)) is True

def test_leitura_estado_personagens():
    pasta_dinamico = root_dir / "background" / "dinamico"
    gerenciador = GerenciadorEstado(str(pasta_dinamico))
    dados = gerenciador.ler_estado("estado_personagens.json")
    
    assert "protagonista" in dados
    assert "saude" in dados["protagonista"]
