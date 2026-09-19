import json
import sys
import random
from pathlib import Path
from typing import Dict, Any, List, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class GerenciadorMemoriaInterconectada:
    """Gerencia a memória modular de entidades com pesos de tempo de tela, tags de subtramas e rastreabilidade por links de linhas/arquivos."""

    def __init__(self, pasta_dinamico: Optional[str] = None):
        if pasta_dinamico:
            self.pasta_dinamico = Path(pasta_dinamico)
        else:
            self.pasta_dinamico = Path(__file__).resolve().parent.parent.parent / "background" / "dinamico"
        self.arquivo_memoria = self.pasta_dinamico / "memoria_interconectada.json"

    def carregar(self) -> Dict[str, Any]:
        """Carrega o índice de memória interconectada."""
        if not self.arquivo_memoria.exists():
            return {"versao_schema": "1.0", "entidades": []}
        with open(self.arquivo_memoria, 'r', encoding='utf-8') as f:
            return json.load(f)

    def salvar(self, dados: Dict[str, Any]) -> None:
        """Salva as alterações no arquivo de memória interconectada."""
        with open(self.arquivo_memoria, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    def obter_entidade(self, id_entidade: str) -> Optional[Dict[str, Any]]:
        """Busca uma entidade específica por ID."""
        dados = self.carregar()
        for ent in dados.get("entidades", []):
            if ent.get("id") == id_entidade:
                return ent
        return None

    def cadastrar_entidade(
        self,
        id_entidade: str,
        nome: str,
        tipo: str,
        descricao: str,
        peso: int = 5,
        tags: Optional[List[str]] = None,
        aparicao_inicial: Optional[Dict[str, str]] = None,
        conexoes: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """Cadastra ou atualiza uma entidade com peso, tags e aparição inicial."""
        dados = self.carregar()
        entidades = dados.setdefault("entidades", [])
        
        # Verifica se já existe para atualizar
        existente = next((e for e in entidades if e.get("id") == id_entidade), None)
        if existente:
            existente["nome"] = nome
            existente["tipo"] = tipo
            existente["descricao"] = descricao
            existente["peso"] = max(1, peso)
            if tags is not None:
                existente["tags"] = list(set(existente.get("tags", []) + tags))
            if aparicao_inicial:
                existente.setdefault("aparicoes", []).append(aparicao_inicial)
            if conexoes:
                existente.setdefault("conexoes", []).extend(conexoes)
            self.salvar(dados)
            return existente

        nova_entidade = {
            "id": id_entidade,
            "nome": nome,
            "tipo": tipo,
            "peso": max(1, peso),
            "status": "ativo",
            "tags": tags or [],
            "descricao": descricao,
            "aparicoes": [aparicao_inicial] if aparicao_inicial else [],
            "conexoes": conexoes or []
        }
        entidades.append(nova_entidade)
        self.salvar(dados)
        return nova_entidade

    def registrar_aparicao(self, id_entidade: str, arquivo: str, linhas: str, contexto: str) -> bool:
        """Adiciona um link de arquivo e intervalo de linhas onde o elemento foi citado/apareceu."""
        dados = self.carregar()
        entidade = next((e for e in dados.get("entidades", []) if e.get("id") == id_entidade), None)
        if not entidade:
            return False
            
        aparicao = {
            "arquivo": arquivo,
            "linhas": linhas,
            "contexto": contexto
        }
        entidade.setdefault("aparicoes", []).append(aparicao)
        self.salvar(dados)
        return True

    def ajustar_peso(self, id_entidade: str, delta: int) -> Optional[int]:
        """Aumenta ou diminui o peso de uma entidade (modifica a probabilidade de tempo de tela)."""
        dados = self.carregar()
        entidade = next((e for e in dados.get("entidades", []) if e.get("id") == id_entidade), None)
        if not entidade:
            return None
            
        novo_peso = max(1, entidade.get("peso", 5) + delta)
        entidade["peso"] = novo_peso
        self.salvar(dados)
        return novo_peso

    def buscar_por_tags(self, tags_desejadas: List[str], tipo: Optional[str] = None) -> List[Dict[str, Any]]:
        """Retorna entidades ativas que contenham pelo menos uma das tags especificadas."""
        dados = self.carregar()
        resultados = []
        tags_set = set(t.lower() for t in tags_desejadas)
        
        for ent in dados.get("entidades", []):
            if ent.get("status") != "ativo":
                continue
            if tipo and ent.get("tipo") != tipo:
                continue
            ent_tags = set(t.lower() for t in ent.get("tags", []))
            if tags_set.intersection(ent_tags):
                resultados.append(ent)
                
        return resultados

    def sortear_entidade_por_peso(
        self,
        tipo: Optional[str] = None,
        tags_filtro: Optional[List[str]] = None
    ) -> Optional[Dict[str, Any]]:
        """Sorteia uma entidade ativa considerando seus pesos e filtros de tipo/tags."""
        dados = self.carregar()
        candidatos = []
        
        for ent in dados.get("entidades", []):
            if ent.get("status") != "ativo":
                continue
            if tipo and ent.get("tipo") != tipo:
                continue
            if tags_filtro:
                tags_filtro_set = set(t.lower() for t in tags_filtro)
                ent_tags = set(t.lower() for t in ent.get("tags", []))
                if not tags_filtro_set.intersection(ent_tags):
                    continue
            candidatos.append(ent)
            
        if not candidatos:
            return None
            
        pesos = [c.get("peso", 1) for c in candidatos]
        return random.choices(candidatos, weights=pesos, k=1)[0]

    def exibir_painel_entidades(self) -> None:
        """Exibe o painel de entidades interconectadas com links de linhas e pesos."""
        dados = self.carregar()
        entidades = dados.get("entidades", [])
        
        print("\n=======================================================")
        print("🕸️ MEMÓRIA MODULAR INTERCONECTADA (ENTIDADES & CENÁRIO)")
        print("=======================================================")
        print(f"Total de entidades registradas: {len(entidades)}\n")
        
        tipos_icones = {
            "personagem": "👤",
            "item": "🗡️",
            "local": "📍",
            "poder": "⚡",
            "faccao": "🚩",
            "evento": "📜"
        }
        
        for ent in entidades:
            icone = tipos_icones.get(ent.get("tipo", ""), "🔹")
            print(f"{icone} [{ent.get('id')}] {ent.get('nome')} | Peso: {ent.get('peso')} | Status: {ent.get('status')}")
            print(f"   📝 Descrição: {ent.get('descricao')}")
            print(f"   🏷️ Tags: {', '.join(ent.get('tags', []))}")
            
            aparicoes = ent.get("aparicoes", [])
            if aparicoes:
                print("   🔗 Links / Aparições:")
                for ap in aparicoes:
                    print(f"      - [{ap.get('arquivo')} : L{ap.get('linhas')}] ➔ {ap.get('contexto')}")
            if ent.get("conexoes"):
                conexoes_str = [f"{c.get('entidade_id')} ({c.get('relacao')})" for c in ent.get("conexoes")]
                print(f"   🪢 Conexões: {', '.join(conexoes_str)}")
            print("-" * 55)
        print("=======================================================\n")

if __name__ == "__main__":
    gerenciador = GerenciadorMemoriaInterconectada()
    gerenciador.exibir_painel_entidades()
