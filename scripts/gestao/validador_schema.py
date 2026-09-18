import json
from pathlib import Path

CAMPOS_OBRIGATORIOS = {
    "estado_mundo.json": ["localizacao_atual", "condicao_climatica", "faccoes_status"],
    "estado_personagens.json": ["protagonista", "relacionamentos"],
    "estado_trama.json": ["arco_narrativo_atual", "capitulo_atual_num", "ganchos_abertos"]
}

def validar_integridade_schemas(pasta_dinamico: str = "background/dinamico") -> bool:
    pasta = Path(pasta_dinamico)
    tudo_valido = True
    
    for arquivo, campos in CAMPOS_OBRIGATORIOS.items():
        caminho = pasta / arquivo
        if not caminho.exists():
            print(f"❌ [ERRO] Arquivo ausente: {arquivo}")
            tudo_valido = False
            continue
        
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
        for campo in campos:
            if campo not in dados:
                print(f"❌ [ERRO] Campo obrigatório '{campo}' ausente em {arquivo}")
                tudo_valido = False
                
    if tudo_valido:
        print("✅ [OK] Todos os schemas de estado dinâmico estão válidos e íntegros!")
    return tudo_valido

if __name__ == "__main__":
    caminho_script = Path(__file__).parent
    pasta_dinamico = caminho_script.parent.parent / "background" / "dinamico"
    validar_integridade_schemas(str(pasta_dinamico))
