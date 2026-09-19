import os
import sys
import json
import shutil
import random
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DIR_FIXO = BASE_DIR / "background" / "fixo"
DIR_DINAMICO = BASE_DIR / "background" / "dinamico"
DIR_PRESETS = BASE_DIR / "background" / "presets"
DIR_ORACULOS = BASE_DIR / "oraculos"

def reseta_estado_dinamico():
    """Reseta todos os arquivos JSON de estado dinâmico e memória volátil para o Capítulo 1."""
    DIR_DINAMICO.mkdir(parents=True, exist_ok=True)
    
    mundo = {
        "localizacao_atual": "Ponto de Partida",
        "distrito_ou_regiao": "Setor Inicial",
        "condicao_climatica": {
            "clima": "Tempo Nublado",
            "temperatura": "Ameno",
            "visibilidade": "Boa",
            "toxidade_ar": "Segura"
        },
        "hora_do_dia": "Manhã",
        "dia_da_saga": 1,
        "nivel_alerta_geral": "Baixo",
        "faccoes_status": {
            "Consórcio": {
                "atitude": "Neutra",
                "nivel_vigilancia": "Baixa",
                "influencia_local": "Moderada"
            },
            "Sindicato_Livre": {
                "atitude": "Neutra",
                "nivel_vigilancia": "Baixa",
                "influencia_local": "Baixa"
            }
        },
        "relogios_urgencia": [],
        "eventos_globais_ativos": []
    }
    
    personagens = {
        "protagonista": {
            "nome": "Protagonista",
            "saude": 100,
            "sanidade_ou_estresse": 0,
            "condicao_fisica": "Saudável",
            "ferimentos_ativos": [],
            "inventario": [
                {
                    "item": "Kit de Primeiros Socorros Básico",
                    "quantidade": 1,
                    "tipo": "consumivel"
                },
                {
                    "item": "Cantil de Água",
                    "quantidade": 1,
                    "tipo": "suprimento"
                }
            ],
            "equipamentos_ativos": {
                "arma_primaria": "Faca de Caça",
                "vestimenta": "Roupas Resistentes de Viajante",
                "item_especial": "Nenhum"
            },
            "habilidades_destaque": []
        },
        "companheiros_ativos": [],
        "relacionamentos": {}
    }
    
    trama = {
        "arco_narrativo_atual": "Início da Saga — O Chamado e o Primeiro Passo",
        "capitulo_atual_num": 1,
        "foco_dramatico_atual": "Descobrir o primeiro objetivo e garantir um abrigo seguro",
        "ganchos_abertos": [
            {
                "id": "gancho_01",
                "descricao": "Descobrir a origem da mensagem misteriosa e o primeiro objetivo da jornada",
                "prioridade": "Alta",
                "capitulo_origem": 1,
                "status": "ativo"
            }
        ],
        "segredos_descobertos": [],
        "historico_capitulos": []
    }
    
    memoria_cena = {
        "capitulo_em_andamento": 1,
        "estagio_cena_atual": "1_entrada",
        "tensao_calibrada": "Moderado",
        "localizacao_cena": "Ponto de Partida",
        "oraculo_ativo_cena": {
            "foco_ou_semente": "Exploração inicial da área desconhecida",
            "reviravolta_prevista": "Nenhuma engatilhada",
            "npc_em_destaque": "Nenhum"
        },
        "buffer_acoes_recentes": [],
        "modificadores_temporarios": [],
        "dialogos_pendentes": [],
        "recursos_gastos_neste_capitulo": {
            "dano_sofrido": 0,
            "itens_consumidos": [],
            "itens_obtidos": []
        }
    }
    
    with open(DIR_DINAMICO / "estado_mundo.json", "w", encoding="utf-8") as f:
        json.dump(mundo, f, indent=2, ensure_ascii=False)
    with open(DIR_DINAMICO / "estado_personagens.json", "w", encoding="utf-8") as f:
        json.dump(personagens, f, indent=2, ensure_ascii=False)
    with open(DIR_DINAMICO / "estado_trama.json", "w", encoding="utf-8") as f:
        json.dump(trama, f, indent=2, ensure_ascii=False)
    with open(DIR_DINAMICO / "memoria_cena.json", "w", encoding="utf-8") as f:
        json.dump(memoria_cena, f, indent=2, ensure_ascii=False)
        
    print("🧹 Estado dinâmico e memória volátil resetados com sucesso para o Capítulo 1.")

def inicializar_manual():
    print("📝 Modo Manual selecionado. Mantendo/Gerando templates limpos em background/fixo/")
    reseta_estado_dinamico()

def inicializar_preset(nome_preset: str):
    pasta_src = DIR_PRESETS / nome_preset
    if not pasta_src.exists():
        print(f"❌ Preset '{nome_preset}' não foi encontrado em {DIR_PRESETS}")
        return False
    
    DIR_FIXO.mkdir(parents=True, exist_ok=True)
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
    print("🎲 Modo Semi-Aleatório Procedural (Oráculo + Adjetivos + Peculiaridades)...\n")
    arquivo_oraculo = DIR_ORACULOS / "geracao_mundo.json"
    if not arquivo_oraculo.exists():
        print(f"❌ Oráculo de geração de mundo não encontrado: {arquivo_oraculo}")
        return
        
    with open(arquivo_oraculo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        
    def pick_weighted(lista):
        if not lista:
            return {"item": "N/A"}
        pesos = [item.get("peso", 1) for item in lista]
        return random.choices(lista, weights=pesos, k=1)[0]
        
    genero = pick_weighted(dados.get("generos", []))["item"]
    atmosfera = pick_weighted(dados.get("adjetivos_atmosfera", []))["item"]
    peculiaridade = pick_weighted(dados.get("peculiaridades_mundo", []))["item"]
    tom = pick_weighted(dados.get("tomes_narrativos", []))["item"]
    conflito = pick_weighted(dados.get("conflitos_centrais", []))["item"]
    origem = pick_weighted(dados.get("origens_protagonista", []))["item"]
    segredo = pick_weighted(dados.get("segredos_protagonista", []))["item"]
    
    premissa_combinada = f"Um universo de {genero} com atmosfera {atmosfera}. {peculiaridade}. O tom é {tom}."
    
    sorteio = {
        "genero_base": genero,
        "adjetivo_atmosfera": atmosfera,
        "peculiaridade_unica_do_mundo": peculiaridade,
        "tom_narrativo": tom,
        "conflito_central": conflito,
        "origem_protagonista": origem,
        "segredo_protagonista": segredo,
        "síntese_atmosférica": premissa_combinada
    }
    
    print("=================================================================")
    print("🌟 PREMISSA PROCEDURAL COMBINATÓRIA GERADA PELO ORÁCULO")
    print("=================================================================")
    print(json.dumps(sorteio, indent=2, ensure_ascii=False))
    print("=================================================================\n")
    print("👉 A LLM deve usar essa semente rica para sintetizar 'background/fixo/'\n")
    
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
        print("2. Semi-Aleatório (Sorteio Combinatório via Oráculo)")
        print("3. Usar Preset (backrooms / game_of_thrones / fantasia_sombria / cyberpunk_noir)")
        choice = input("Escolha uma opção (1, 2 ou 3): ").strip()
        if choice == "1":
            inicializar_manual()
        elif choice == "2":
            inicializar_oraculo()
        elif choice == "3":
            preset = input("Digite o nome do preset (ex: backrooms, game_of_thrones, fantasia_sombria, cyberpunk_noir): ").strip()
            inicializar_preset(preset)
