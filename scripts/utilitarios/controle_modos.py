import json
from pathlib import Path

MODOS_PERMITIDOS = ["coautor", "interativo", "edicao", "adicao"]

def obter_modo_atual(caminho_config: str = "config/config_geral.json") -> str:
    path = Path(caminho_config)
    if not path.exists():
        return "coautor"
    with open(path, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        return dados.get("modo_ativo", "coautor")

def definir_modo_ativo(novo_modo: str, caminho_config: str = "config/config_geral.json") -> bool:
    if novo_modo not in MODOS_PERMITIDOS:
        print(f"❌ Modo inválido: {novo_modo}. Escolha entre: {MODOS_PERMITIDOS}")
        return False
    path = Path(caminho_config)
    if not path.exists():
        dados = {}
    else:
        with open(path, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    dados["modo_ativo"] = novo_modo
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    print(f"🔄 Modo de operação alterado para: [{novo_modo}]")
    return True

if __name__ == "__main__":
    caminho_script = Path(__file__).parent
    config_file = caminho_script.parent.parent / "config" / "config_geral.json"
    print("Modo Atual:", obter_modo_atual(str(config_file)))
