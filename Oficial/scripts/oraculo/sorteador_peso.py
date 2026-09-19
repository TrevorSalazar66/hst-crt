import json
import random
from pathlib import Path
from typing import Dict, Any, List

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

    def sortear_de_lista(self, opcoes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Sorteia um item de uma lista de opções ponderadas."""
        if not opcoes:
            raise ValueError("Lista de opções está vazia.")
        pesos = [opcao.get("peso", 1) for opcao in opcoes]
        return random.choices(opcoes, weights=pesos, k=1)[0]

    def sortear_item(self, nome_arquivo: str, chave: str = "opcoes") -> Dict[str, Any]:
        """Realiza um sorteio ponderado simples em uma chave de lista."""
        dados = self.carregar_tabela(nome_arquivo)
        opcoes = dados.get(chave, [])
        if not opcoes:
            raise ValueError(f"Chave '{chave}' não encontrada ou vazia em {nome_arquivo}.")
        
        item_sorteado = self.sortear_de_lista(opcoes)
        return {
            "tabela": dados.get("nome_tabela", nome_arquivo),
            "item": item_sorteado.get("item"),
            "descricao": item_sorteado.get("descricao", ""),
            "peso": item_sorteado.get("peso")
        }

    def sortear_semente_cena(self) -> Dict[str, Any]:
        """Sorteia uma semente de cena modular com tipo, dinâmica detalhada, objetivo e urgência."""
        dados = self.carregar_tabela("sementes_cena.json")
        tipo = self.sortear_de_lista(dados.get("tipos_cena", []))
        item_tipo = tipo.get("item", "")

        mapeamento_tipo = {
            "Investigação e Descoberta de Mistério": "cenas_investigacao",
            "Infiltração e Operação Furtiva": "cenas_infiltracao",
            "Confronto Direto e Embate Físico": "cenas_confronto",
            "Negociação Tensa e Diplomacia Suja": "cenas_negociacao",
            "Sobrevivência, Fuga e Perseguição": "cenas_sobrevivencia",
            "Operação Técnica, Cura e Ritual Clandestino": "cenas_operacao_tecnica",
            "Respiro Dramático, Confissão e Vínculos": "cenas_respiro_dramatico"
        }

        chave_dinamica = mapeamento_tipo.get(item_tipo)
        if chave_dinamica and chave_dinamica in dados:
            dinamica = self.sortear_de_lista(dados[chave_dinamica])
        else:
            dinamica = tipo

        objetivo = self.sortear_de_lista(dados.get("objetivos_imediatos", []))
        urgencia = self.sortear_de_lista(dados.get("fatores_pressao_urgencia", []))

        return {
            "tipo_cena": tipo.get("item"),
            "dinamica_especifica": dinamica.get("item"),
            "dinamica_descricao": dinamica.get("descricao", ""),
            "objetivo_imediato": objetivo.get("item"),
            "objetivo_descricao": objetivo.get("descricao", ""),
            "fator_urgencia": urgencia.get("item"),
            "urgencia_descricao": urgencia.get("descricao", "")
        }

    def sortear_reviravolta(self) -> Dict[str, Any]:
        """Sorteia uma reviravolta categorizada ou indica ausência de complicação."""
        dados = self.carregar_tabela("reviravoltas.json")
        controle = self.sortear_de_lista(dados.get("controle_ocorrencia", []))
        
        item_controle = controle.get("item", "")
        if "Nenhuma Reviravolta" in item_controle:
            return {
                "ocorreu": False,
                "categoria": "Nenhuma",
                "item": item_controle,
                "descricao": controle.get("descricao", "")
            }
        
        mapeamento = {
            "Revelações e Enganos": "revelacoes_e_enganos",
            "Interrupções e Terceiras Facções": "interrupcoes_e_terceiras_faccoes",
            "Anomalias Ambientais e Colapso do Cenário": "anomalias_ambientais_e_cenario",
            "Falhas Críticas de Recursos e Equipamento": "falhas_de_recursos_e_equipamento",
            "Dilemas Morais Repentinos e Conflitos de Lealdade": "dilemas_morais_e_conflitos_lealdade"
        }
        
        chave_categoria = mapeamento.get(item_controle)
        if chave_categoria and chave_categoria in dados:
            detalhe = self.sortear_de_lista(dados[chave_categoria])
            return {
                "ocorreu": True,
                "categoria": item_controle,
                "item": detalhe.get("item"),
                "descricao": detalhe.get("descricao", "")
            }
        
        return {
            "ocorreu": True,
            "categoria": item_controle,
            "item": item_controle,
            "descricao": controle.get("descricao", "")
        }

if __name__ == "__main__":
    caminho_base = Path(__file__).resolve().parent.parent.parent / "Oficial" / "oraculos"
    sorteador = SorteadorOraculo(str(caminho_base))
    res_cena = sorteador.sortear_semente_cena()
    print("Sorteio de Cena Modular:", json.dumps(res_cena, indent=2, ensure_ascii=False))
