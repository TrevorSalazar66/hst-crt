import os
import sys
import json
import random
from pathlib import Path
from typing import Dict, Any, List, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class GeradorProceduralBackrooms:
    """Motor procedural de sorteio modular para o universo das Backrooms."""

    def __init__(self, pasta_oraculos: Optional[str] = None):
        if pasta_oraculos:
            self.pasta_oraculos = Path(pasta_oraculos)
        else:
            self.pasta_oraculos = Path(__file__).resolve().parent.parent / "oraculos"

    def carregar_tabela(self, nome_arquivo: str) -> Dict[str, Any]:
        caminho = self.pasta_oraculos / nome_arquivo
        if not caminho.exists():
            raise FileNotFoundError(f"Tabela de oráculo não encontrada: {caminho}")
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def sortear_de_lista(self, lista: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not lista:
            return {"item": "N/A"}
        pesos = [elem.get("peso", 1) for elem in lista]
        return random.choices(lista, weights=pesos, k=1)[0]

    # -------------------------------------------------------------------------
    # Métodos de Geração Modular
    # -------------------------------------------------------------------------

    def gerar_nivel(self, numero_nivel_sugerido: Optional[int] = None) -> Dict[str, Any]:
        """Gera um nível liminar aleatório e único."""
        dados = self.carregar_tabela("gerador_niveis.json")
        num = numero_nivel_sugerido if numero_nivel_sugerido is not None else random.randint(0, 999)
        
        classe = self.sortear_de_lista(dados.get("classes_sobrevivencia", []))["item"]
        tema = self.sortear_de_lista(dados.get("temas_arquitetura", []))["item"]
        luz = self.sortear_de_lista(dados.get("iluminacao_e_zumbido", []))["item"]
        perigo = self.sortear_de_lista(dados.get("perigos_ambientais", []))["item"]
        anomalia = self.sortear_de_lista(dados.get("anomalias_especiais", []))["item"]
        noclip = self.sortear_de_lista(dados.get("gatilhos_de_noclip", []))["item"]
        
        return {
            "identificador_nivel": f"Nível {num}",
            "classe_seguranca": classe,
            "arquitetura_ambiente": tema,
            "iluminacao_e_som": luz,
            "perigo_ambiental_dominante": perigo,
            "anomalia_ou_recurso": anomalia,
            "metodo_saida_noclip": noclip
        }

    def gerar_entidade(self) -> Dict[str, Any]:
        """Gera uma criatura/entidade anômala com táticas e fraquezas."""
        dados = self.carregar_tabela("gerador_entidades.json")
        
        arquetipo = self.sortear_de_lista(dados.get("arquetipos_entidades", []))["item"]
        aparencia = self.sortear_de_lista(dados.get("aparencias_e_detalhes", []))["item"]
        comportamento = self.sortear_de_lista(dados.get("comportamentos_e_taticas", []))["item"]
        fraqueza = self.sortear_de_lista(dados.get("fraquezas_e_contramedidas", []))["item"]
        som = self.sortear_de_lista(dados.get("sons_caracteristicos", []))["item"]
        despojo = self.sortear_de_lista(dados.get("recompensas_despojos", []))["item"]
        
        return {
            "entidade_tipo": arquetipo,
            "detalhes_visuais": aparencia,
            "tatica_de_caca": comportamento,
            "contramedida_sobrevivencia": fraqueza,
            "ruido_emitido": som,
            "despojo_possivel": despojo
        }

    def gerar_organizacao(self) -> Dict[str, Any]:
        """Gera um posto avançado de facção ou grupo de sobreviventes."""
        dados = self.carregar_tabela("gerador_organizacoes.json")
        
        faccao = self.sortear_de_lista(dados.get("organizacoes_faccoes", []))["item"]
        posto = self.sortear_de_lista(dados.get("postos_avancados", []))["item"]
        atitude = self.sortear_de_lista(dados.get("atitudes_iniciais", []))["item"]
        servico = self.sortear_de_lista(dados.get("servicos_e_comercio", []))["item"]
        segredo = self.sortear_de_lista(dados.get("segredos_e_conflitos", []))["item"]
        
        return {
            "faccao": faccao,
            "instalacao_posto": posto,
            "atitude_inicial": atitude,
            "comercio_e_suporte": servico,
            "segredo_ou_crise": segredo
        }

    def gerar_loot_itens(self) -> Dict[str, Any]:
        """Gera um pacote de suprimentos e relíquias encontradas no ambiente."""
        dados = self.carregar_tabela("gerador_itens.json")
        
        fluido = self.sortear_de_lista(dados.get("fluidos_e_liquidos", []))["item"]
        ferramenta = self.sortear_de_lista(dados.get("ferramentas_e_eletronicos", []))["item"]
        suprimento = self.sortear_de_lista(dados.get("suprimentos_e_sobrevivencia", []))["item"]
        arma = self.sortear_de_lista(dados.get("armamento_improvisado", []))["item"]
        reliquia = self.sortear_de_lista(dados.get("reliquias_liminares", []))["item"]
        
        return {
            "fluido_encontrado": fluido,
            "eletronico_ou_luz": ferramenta,
            "suprimento_vital": suprimento,
            "arma_ou_ferramenta": arma,
            "reliquia_anomala": reliquia
        }

    def gerar_encontro_completo(self) -> Dict[str, Any]:
        """Gera uma cena completa contendo Nível + Entidade ou Facção + Loot."""
        nivel = self.gerar_nivel()
        tem_faccao = random.random() < 0.4  # 40% de chance de encontrar posto de sobreviventes
        
        resultado = {
            "cenario_nivel": nivel,
            "loot_descoberto": self.gerar_loot_itens()
        }
        
        if tem_faccao:
            resultado["encontro_social"] = self.gerar_organizacao()
        else:
            resultado["ameaca_entidade"] = self.gerar_entidade()
            
        return resultado

    # -------------------------------------------------------------------------
    # Impressão Visual Formatada
    # -------------------------------------------------------------------------

    def imprimir_nivel(self, dados: Dict[str, Any]) -> None:
        print("\n=======================================================")
        print(f"🏢 GERADOR PROCEDURAL: {dados['identificador_nivel']}")
        print("=======================================================")
        print(f"🚨 Segurança: {dados['classe_seguranca']}")
        print(f"🏛️ Arquitetura: {dados['arquitetura_ambiente']}")
        print(f"💡 Luz & Som: {dados['iluminacao_e_som']}")
        print(f"⚠️ Perigo Ambiental: {dados['perigo_ambiental_dominante']}")
        print(f"✨ Anomalia / Recurso: {dados['anomalia_ou_recurso']}")
        print(f"🌀 Rota de No-Clip: {dados['metodo_saida_noclip']}")
        print("=======================================================\n")

    def imprimir_entidade(self, dados: Dict[str, Any]) -> None:
        print("\n=======================================================")
        print(f"👾 ENTIDADE ANÔMALA: {dados['entidade_tipo']}")
        print("=======================================================")
        print(f"👁️ Aparência: {dados['detalhes_visuais']}")
        print(f"🎯 Método de Caça: {dados['tatica_de_caca']}")
        print(f"🛡️ Como Sobreviver: {dados['contramedida_sobrevivencia']}")
        print(f"🔊 Ruído: {dados['ruido_emitido']}")
        print(f"📦 Despojo: {dados['despojo_possivel']}")
        print("=======================================================\n")

    def imprimir_organizacao(self, dados: Dict[str, Any]) -> None:
        print("\n=======================================================")
        print(f"🚩 ORGANIZAÇÃO / FACÇÃO: {dados['faccao']}")
        print("=======================================================")
        print(f"⛺ Posto: {dados['instalacao_posto']}")
        print(f"🤝 Atitude Inicial: {dados['atitude_inicial']}")
        print(f"🛒 Serviços / Trocas: {dados['comercio_e_suporte']}")
        print(f"🤫 Segredo Oculto: {dados['segredo_ou_crise']}")
        print("=======================================================")

    def imprimir_loot(self, dados: Dict[str, Any]) -> None:
        print("\n=======================================================")
        print("🎒 LOOT & SUPRIMENTOS LIMINARES DESCOBERTOS")
        print("=======================================================")
        print(f"💧 Fluido: {dados['fluido_encontrado']}")
        print(f"🔋 Eletrônico/Luz: {dados['eletronico_ou_luz']}")
        print(f"🥫 Suprimento: {dados['suprimento_vital']}")
        print(f"🗡️ Arma/Ferramenta: {dados['arma_ou_ferramenta']}")
        print(f"📜 Relíquia: {dados['reliquia_anomala']}")
        print("=======================================================\n")

if __name__ == "__main__":
    gerador = GeradorProceduralBackrooms()
    
    comando = sys.argv[1].lower() if len(sys.argv) > 1 else "tudo"
    
    if comando in ["nivel", "cenario"]:
        gerador.imprimir_nivel(gerador.gerar_nivel())
    elif comando in ["entidade", "monstro"]:
        gerador.imprimir_entidade(gerador.gerar_entidade())
    elif comando in ["faccao", "organizacao", "posto"]:
        gerador.imprimir_organizacao(gerador.gerar_organizacao())
    elif comando in ["loot", "itens", "suprimentos"]:
        gerador.imprimir_loot(gerador.gerar_loot_itens())
    elif comando == "tudo":
        encontro = gerador.gerar_encontro_completo()
        gerador.imprimir_nivel(encontro["cenario_nivel"])
        if "ameaca_entidade" in encontro:
            gerador.imprimir_entidade(encontro["ameaca_entidade"])
        if "encontro_social" in encontro:
            gerador.imprimir_organizacao(encontro["encontro_social"])
        gerador.imprimir_loot(encontro["loot_descoberto"])
    elif comando == "json":
        print(json.dumps(gerador.gerar_encontro_completo(), indent=2, ensure_ascii=False))
    else:
        print("Uso: python gerador_backrooms.py [nivel|entidade|faccao|loot|tudo|json]")
