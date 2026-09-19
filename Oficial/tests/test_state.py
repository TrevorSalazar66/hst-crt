import pytest
import sys
import json
import tempfile
import shutil
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir / "scripts" / "gestao"))
sys.path.append(str(root_dir / "scripts" / "utilitarios"))

from gerenciador_estado import GerenciadorEstado
from memoria_volatil import BufferMemoriaVolatil
from validador_schema import validar_integridade_schemas
from gerenciador_memoria_interconectada import GerenciadorMemoriaInterconectada
from formatador_capitulo import formatar_cabecalho_capitulo, formatar_rodape_consequencias

@pytest.fixture
def pasta_dinamico_temp():
    """Cria uma pasta temporária com os arquivos de estado para não poluir os dados oficiais nos testes."""
    temp_dir = Path(tempfile.mkdtemp())
    origem = root_dir / "background" / "dinamico"
    for item in origem.iterdir():
        if item.is_file():
            shutil.copy2(item, temp_dir)
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_validacao_schemas_oficiais():
    pasta_dinamico = root_dir / "background" / "dinamico"
    assert validar_integridade_schemas(str(pasta_dinamico)) is True

def test_leitura_e_manipulacao_saude(pasta_dinamico_temp):
    gerenciador = GerenciadorEstado(str(pasta_dinamico_temp))
    
    # Aplica dano
    nova_saude = gerenciador.aplicar_dano_saude(30, "Corte no braço")
    assert nova_saude == 70
    
    personagens = gerenciador.ler_estado("estado_personagens.json")
    assert "Corte no braço" in personagens["protagonista"]["ferimentos_ativos"]
    assert personagens["protagonista"]["condicao_fisica"] == "Ferido"
    
    # Aplica cura
    saude_curada = gerenciador.curar_saude(20, "Corte no braço")
    assert saude_curada == 90
    personagens_pos_cura = gerenciador.ler_estado("estado_personagens.json")
    assert "Corte no braço" not in personagens_pos_cura["protagonista"]["ferimentos_ativos"]

def test_manipulacao_inventario(pasta_dinamico_temp):
    gerenciador = GerenciadorEstado(str(pasta_dinamico_temp))
    
    gerenciador.adicionar_item_inventario("Gazua Reforçada", quantidade=2, tipo="ferramenta")
    sucesso_consumo = gerenciador.consumir_item_inventario("Gazua Reforçada", quantidade=1)
    assert sucesso_consumo is True
    
    personagens = gerenciador.ler_estado("estado_personagens.json")
    inventario = personagens["protagonista"]["inventario"]
    gazua = next((i for i in inventario if i.get("item") == "Gazua Reforçada"), None)
    assert gazua is not None
    assert gazua["quantidade"] == 1

def test_ganchos_e_relogios_urgencia(pasta_dinamico_temp):
    gerenciador = GerenciadorEstado(str(pasta_dinamico_temp))
    
    id_gancho = gerenciador.adicionar_gancho("Encontrar a chave mestra", prioridade="Alta")
    assert id_gancho is not None
    
    atualizado = gerenciador.atualizar_status_gancho(id_gancho, "resolvido")
    assert atualizado is True
    
    # Relógio de urgência
    gerenciador.adicionar_relogio_urgencia("Contaminação por Névoa", turnos_max=2, consequencia="Dano contínuo")
    alertas = gerenciador.avancar_relogios_urgencia(2)
    assert len(alertas) == 1
    assert "RELÓGIO ENGATILHADO" in alertas[0]

def test_buffer_memoria_volatil(pasta_dinamico_temp):
    buffer = BufferMemoriaVolatil(str(pasta_dinamico_temp))
    buffer.resetar_buffer(numero_capitulo=2, tensao="Alto", local="Docas Abandonadas")
    
    buffer.definir_oraculo_cena("Infiltração Furtiva", "Patrulha Surpresa", "Guarda Corrupto")
    buffer.registrar_acao("Protagonista", "Escondeu-se nas sombras")
    buffer.registrar_gasto_item("Filtro de Ar", 1)
    buffer.registrar_dano_sofrido(15)
    
    dados = buffer.carregar()
    assert dados["capitulo_em_andamento"] == 2
    assert dados["tensao_calibrada"] == "Alto"
    assert dados["recursos_gastos_neste_capitulo"]["dano_sofrido"] == 15

def test_memoria_interconectada(pasta_dinamico_temp):
    ger_mem = GerenciadorMemoriaInterconectada(str(pasta_dinamico_temp))
    
    entidade = ger_mem.cadastrar_entidade(
        id_entidade="npc_mestre_alquimista",
        nome="Eldrin, o Alquimista Cego",
        tipo="personagem",
        descricao="Especialista em toxinas e destilação de elixires.",
        peso=7,
        tags=["alquimia", "submundo", "distrito_baixo"],
        aparicao_inicial={"arquivo": "saga/capitulo_02.md", "linhas": "10-25", "contexto": "Primeira consulta de antídoto"}
    )
    assert entidade["id"] == "npc_mestre_alquimista"
    assert entidade["peso"] == 7
    
    # Adicionar nova aparição
    sucesso_ap = ger_mem.registrar_aparicao("npc_mestre_alquimista", "saga/capitulo_04.md", "30-45", "Entregou frasco de elixir")
    assert sucesso_ap is True
    
    # Ajustar peso
    novo_peso = ger_mem.ajustar_peso("npc_mestre_alquimista", +2)
    assert novo_peso == 9
    
    # Busca por tags
    encontrados = ger_mem.buscar_por_tags(["alquimia"])
    assert len(encontrados) >= 1
    
    # Sorteio ponderado por tag
    sorteado = ger_mem.sortear_entidade_por_peso(tags_filtro=["alquimia"])
    assert sorteado is not None
    assert sorteado["id"] == "npc_mestre_alquimista"

def test_formatadores():
    cabecalho = formatar_cabecalho_capitulo(1, "O Início", "Exploração", "Distrito Baixo")
    assert "# Capítulo 01: O Início" in cabecalho
    assert "Estado de Tensão" in cabecalho
    
    rodape = formatar_rodape_consequencias("90% HP", "1x Filtro gasto", "Pista obtida")
    assert "Consequências & Atualizações da Cena" in rodape
