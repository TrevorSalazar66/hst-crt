import json
import random
from pathlib import Path
from typing import Dict, Any, Optional

class SorteadorOraculo:
    """Classe responsável por carregar tabelas JSON e realizar sorteios ponderados."""

    def __init__(self, pasta_oraculos: str = "oraculos"):
        self.pasta_oraculos = Path(pasta_oraculos)

    def carregar_tabela(self, nome_arquivo: str) -> Dict[str, Any]:
        caminho = self.pasta_oraculos / nome_arquivo
        if not caminho.exists():
            raise FileNotFoundError(f"Tabela de oráculo não encontrada: {caminho}")
        
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def sortear_item(self, nome_arquivo: str) -> Dict[str, Any]:
        """Realiza um sorteio ponderado (weighted draw) na tabela especificada."""
        dados = self.carregar_tabela(nome_arquivo)
        opcoes = dados.get("opcoes", [])
        
        if not opcoes:
            raise ValueError(f"Tabela {nome_arquivo} está vazia ou sem opções válidas.")

        pesos = [opcao.get("peso", 1) for opcao in opcoes]
        item_sorteado = random.choices(opcoes, weights=pesos, k=1)[0]
        
        return {
            "tabela": dados.get("nome_tabela", nome_arquivo),
            "item": item_sorteado.get("item"),
            "descricao": item_sorteado.get("descricao", ""),
            "peso": item_sorteado.get("peso")
        }

if __name__ == "__main__":
    sorteador = SorteadorOraculo()
    res = sorteador.sortear_item("sementes_cena.json")
    print("Sorteio de Teste:", res)
