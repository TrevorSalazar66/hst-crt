import os
import sys
import json
import shutil
import random
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DIR_FIXO = BASE_DIR / "background" / "fixo"
DIR_DINAMICO = BASE_DIR / "background" / "dinamico"
DIR_PRESETS = BASE_DIR / "background" / "presets"
DIR_ORACULOS = BASE_DIR / "oraculos"

def reseta_estado_dinamico():
    """Reseta os arquivos JSON de estado para o capitulo 1."""
    mundo = {
        "localizacao_atual": "Ponto de Partida",
        "condicao_climatica": "Normal",
        "hora_do_dia": "Manhã",
        "faccoes_status": {},
        "eventos_globais_ativos": []
    }
    personagens = {
        "protagonista": {"saude": 100, "condicao_fisica": "Saudável", "inventario": []},
        "relacionamentos": {}
    }
    trama = {
        "arco_narrativo_atual": "Início da Saga",
        "capitulo_atual_num": 1,
        "ganchos_abertos": ["Descobrir o primeiro objetivo"],
        "historico_capitulos": []
    }
    
    with open(DIR_DINAMICO / "estado_mundo.json", "w", encoding="utf-8") as f:
        json.dump(mundo, f, indent=2, ensure_ascii=False)
    with open(DIR_DINAMICO / "estado_personagens.json", "w", encoding="utf-8") as f:
        json.dump(personagens, f, indent=2, ensure_ascii=False)
    with open(DIR_DINAMICO / "estado_trama.json", "w", encoding="utf-8") as f:
        json.dump(trama, f, indent=2, ensure_ascii=False)
    print("🧹 Estado dinâmico resetado para o Capítulo 1.")

def inicializar_manual():
    print("📝 Modo Manual selecionado. Mantendo/Gerando templates limpos em background/fixo/")
    reseta_estado_dinamico()

def inicializar_preset(nome_preset: str):
    pasta_src = DIR_PRESETS / nome_preset
    if not pasta_src.exists():
        print(f"❌ Preset '{nome_preset}' não foi encontrado em {DIR_PRESETS}")
        return False
    
    # Copia os arquivos do preset para background/fixo/
    for item in pasta_src.iterdir():
        dest = DIR_FIXO / item.name
        if item.is_dir():
            shutil.copytree(item, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest)
            
    print(f"✅ Cenário pré-pronto '{nome_preset}' carregado com sucesso em background/fixo/")
    reseta_estado_dinamico()
    return True

def inicializar_oraculo():
    print("🎲 Modo Semi-Aleatório (Oráculo). Sortando elementos do universo...")
    arquivo_oraculo = DIR_ORACULOS / "geracao_mundo.json"
    if not arquivo_oraculo.exists():
        print(f"❌ Oráculo de geração de mundo não encontrado: {arquivo_oraculo}")
        return
        
    with open(arquivo_oraculo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        
    def pick_weighted(lista):
        pesos = [item.get("peso", 1) for item in lista]
        return random.choices(lista, weights=pesos, k=1)[0]
        
    genero = pick_weighted(dados.get("generos", []))
    tom = pick_weighted(dados.get("tomes_narrativos", []))
    conflito = pick_weighted(dados.get("conflitos_centrais", []))
    origem = pick_weighted(dados.get("origens_protagonista", []))
    
    sorteio = {
        "genero": genero["item"],
        "tom": tom["item"],
        "conflito_central": conflito["item"],
        "origem_protagonista": origem["item"]
    }
    
    print("\n==========================================")
    print("🌟 ELEMENTOS DE MUNDO SORTEADOS PELO ORÁCULO")
    print("==========================================")
    print(json.dumps(sorteio, indent=2, ensure_ascii=False))
    print("==========================================\n")
    print("👉 Passe esse resultado para a LLM sintetizar a lore em background/fixo/\n")
    reseta_estado_dinamico()
    return sorteio

if __name__ == "__main__":
    if len(sys.argv) > 1:
        opcao = sys.argv[1].lower()
        if opcao == "manual":
            inicializar_manual()
        elif opcao == "oraculo":
            inicializar_oraculo()
        elif opcao.startswith("preset:"):
            nome = opcao.split(":", 1)[1]
            inicializar_preset(nome)
        else:
            print("Uso: python inicializador_saga.py [manual|oraculo|preset:<nome_preset>]")
    else:
        print("--- INICIALIZADOR DE SAGA (BLOCO 1) ---")
        print("1. Manual (Templates limpos)")
        print("2. Semi-Aleatório (Sorteio via Oráculo)")
        print("3. Usar Preset (fantasia_sombria / cyberpunk_noir)")
        choice = input("Escolha uma opção (1, 2 ou 3): ").strip()
        if choice == "1":
            inicializar_manual()
        elif choice == "2":
            inicializar_oraculo()
        elif choice == "3":
            preset = input("Digite o nome do preset (ex: fantasia_sombria ou cyberpunk_noir): ").strip()
            inicializar_preset(preset)
