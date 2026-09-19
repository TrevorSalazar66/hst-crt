import sys
from typing import Dict, Any, List, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def formatar_cabecalho_capitulo(
    numero_capitulo: int,
    titulo: str,
    foco_narrativo: str,
    localizacao: str,
    estado_tensao: str = "Moderado",
    reviravolta: str = "Nenhuma"
) -> str:
    """Gera o cabeçalho padronizado em Markdown para os capítulos da saga."""
    cabecalho = f"""# Capítulo {numero_capitulo:02d}: {titulo}

> **Foco Narrativo:** {foco_narrativo}  
> **Localização:** {localizacao}  
> **Estado de Tensão:** {estado_tensao}  
> **Reviravolta da Cena:** {reviravolta}

---

"""
    return cabecalho

def formatar_rodape_consequencias(
    saude_condicao: str,
    recursos_inventario: str,
    ganchos_segredos: str
) -> str:
    """Gera o bloco final padronizado de Consequências & Atualizações da Cena."""
    rodape = f"""

---

### 📌 Consequências & Atualizações da Cena
* **Saúde & Condição:** {saude_condicao}
* **Recursos & Inventário:** {recursos_inventario}
* **Ganchos & Segredos:** {ganchos_segredos}
"""
    return rodape

if __name__ == "__main__":
    exemplo_cabecalho = formatar_cabecalho_capitulo(
        numero_capitulo=1,
        titulo="Cinzas na Névoa",
        foco_narrativo="Infiltração no galpão abandonado do Distrito Baixo",
        localizacao="Distrito Baixo — Docas Velhas",
        estado_tensao="Alto",
        reviravolta="Patrulha do Consórcio chega antes do esperado"
    )
    exemplo_rodape = formatar_rodape_consequencias(
        saude_condicao="Saudável (90% HP) — corte superficial no antebraço",
        recursos_inventario="Gasto 1x Filtro de Ar | Adquirida 1x Chave de Latão",
        ganchos_segredos="Pista sobre a traição do informante descoberta"
    )
    print("--- EXEMPLO DE CABEÇALHO ---")
    print(exemplo_cabecalho)
    print("--- EXEMPLO DE RODAPÉ ---")
    print(exemplo_rodape)
