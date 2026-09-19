import json
import sys
from pathlib import Path
from typing import Dict, Any, List

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

CAMPOS_OBRIGATORIOS = {
    "estado_mundo.json": [
        "localizacao_atual",
        "condicao_climatica",
        "nivel_alerta_geral",
        "faccoes_status",
        "relogios_urgencia"
    ],
    "estado_personagens.json": [
        "protagonista",
        "companheiros_ativos",
        "relacionamentos"
    ],
    "estado_trama.json": [
        "arco_narrativo_atual",
        "capitulo_atual_num",
        "foco_dramatico_atual",
        "ganchos_abertos",
        "historico_capitulos"
    ],
    "memoria_cena.json": [
        "capitulo_em_andamento",
        "estagio_cena_atual",
        "tensao_calibrada",
        "oraculo_ativo_cena",
        "recursos_gastos_neste_capitulo"
    ],
    "memoria_interconectada.json": [
        "versao_schema",
        "entidades"
    ]
}

def validar_integridade_schemas(pasta_dinamico: str = "background/dinamico") -> bool:
    pasta = Path(pasta_dinamico)
    tudo_valido = True
    erros = []
    
    print("\n🔍 Validando integridade dos schemas JSON de estado dinâmico e memória volátil...")
    
    for arquivo, campos in CAMPOS_OBRIGATORIOS.items():
        caminho = pasta / arquivo
        if not caminho.exists():
            erros.append(f"❌ [ARQUIVO AUSENTE] {arquivo} não foi encontrado em {pasta}")
            tudo_valido = False
            continue
        
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except Exception as e:
            erros.append(f"❌ [JSON INVÁLIDO] Erro ao parsear {arquivo}: {e}")
            tudo_valido = False
            continue
            
        for campo in campos:
            if campo not in dados:
                erros.append(f"❌ [CAMPO FALTANDO] Campo '{campo}' ausente no schema de {arquivo}")
                tudo_valido = False
                
        # Validações lógicas extras
        if arquivo == "estado_personagens.json":
            saude = dados.get("protagonista", {}).get("saude")
            if saude is not None and not (0 <= saude <= 100):
                erros.append(f"⚠️ [VALOR INVÁLIDO] Saúde do protagonista fora do intervalo 0-100: {saude}")
                tudo_valido = False
                
        if arquivo == "estado_trama.json":
            cap = dados.get("capitulo_atual_num")
            if cap is not None and cap < 1:
                erros.append(f"⚠️ [VALOR INVÁLIDO] capitulo_atual_num deve ser >= 1: {cap}")
                tudo_valido = False
                
    if tudo_valido:
        print("✅ [SUCESSO] Todos os 4 arquivos de estado e memória volátil estão 100% íntegros e compatíveis!")
    else:
        print(f"❌ [FALHA] Foram encontrados {len(erros)} erros de schema:")
        for err in erros:
            print(f"   {err}")
            
    return tudo_valido

if __name__ == "__main__":
    caminho_script = Path(__file__).resolve().parent
    pasta_dinamico = caminho_script.parent.parent / "background" / "dinamico"
    validar_integridade_schemas(str(pasta_dinamico))
