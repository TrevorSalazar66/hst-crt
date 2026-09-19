import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class BufferMemoriaVolatil:
    """Gerencia a memória volátil de curto prazo da cena em andamento (memoria_cena.json)."""

    def __init__(self, pasta_dinamico: Optional[str] = None):
        if pasta_dinamico:
            self.pasta_dinamico = Path(pasta_dinamico)
        else:
            self.pasta_dinamico = Path(__file__).resolve().parent.parent.parent / "background" / "dinamico"
        self.arquivo_memoria = self.pasta_dinamico / "memoria_cena.json"

    def carregar(self) -> Dict[str, Any]:
        """Lê o buffer de memória volátil da cena."""
        if not self.arquivo_memoria.exists():
            return self.resetar_buffer(1)
        with open(self.arquivo_memoria, 'r', encoding='utf-8') as f:
            return json.load(f)

    def salvar(self, dados: Dict[str, Any]) -> None:
        """Salva as alterações no buffer de memória volátil."""
        with open(self.arquivo_memoria, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    def resetar_buffer(self, numero_capitulo: int, tensao: str = "Moderado", local: str = "Local Desconhecido") -> Dict[str, Any]:
        """Inicializa um buffer limpo para o início de um novo capítulo."""
        buffer_novo = {
            "capitulo_em_andamento": numero_capitulo,
            "estagio_cena_atual": "1_entrada",
            "tensao_calibrada": tensao,
            "localizacao_cena": local,
            "oraculo_ativo_cena": {
                "foco_ou_semente": "A definir",
                "reviravolta_prevista": "Nenhuma",
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
        self.salvar(buffer_novo)
        return buffer_novo

    def definir_oraculo_cena(self, semente: str, reviravolta: str = "Nenhuma", npc: str = "Nenhum") -> None:
        """Registra a premissa sorteada pelo oráculo no buffer da cena."""
        dados = self.carregar()
        dados["oraculo_ativo_cena"] = {
            "foco_ou_semente": semente,
            "reviravolta_prevista": reviravolta,
            "npc_em_destaque": npc
        }
        self.salvar(dados)

    def avancar_estagio(self, novo_estagio: str) -> None:
        """Atualiza a fase da cena (1_entrada, 2_atrito, 3_inflexao, 4_climax, 5_consequencia)."""
        dados = self.carregar()
        dados["estagio_cena_atual"] = novo_estagio
        self.salvar(dados)

    def registrar_acao(self, autor: str, acao: str) -> None:
        """Adiciona uma ação ou decisão tomada no histórico volátil do turno."""
        dados = self.carregar()
        dados.setdefault("buffer_acoes_recentes", []).append({
            "autor": autor,
            "acao": acao
        })
        self.salvar(dados)

    def adicionar_modificador_temporario(self, nome: str, efeito: str, duracao_turnos: int = 1) -> None:
        """Registra um buff/debuff temporário (ex: cego por gás, adrenalina, etc.)."""
        dados = self.carregar()
        dados.setdefault("modificadores_temporarios", []).append({
            "nome": nome,
            "efeito": efeito,
            "duracao_turnos": duracao_turnos
        })
        self.salvar(dados)

    def registrar_gasto_item(self, item_nome: str, quantidade: int = 1) -> None:
        """Registra consumo de itens na cena corrente."""
        dados = self.carregar()
        gastos = dados.setdefault("recursos_gastos_neste_capitulo", {}).setdefault("itens_consumidos", [])
        gastos.append({"item": item_nome, "quantidade": quantidade})
        self.salvar(dados)

    def registrar_dano_sofrido(self, pontos_dano: int) -> None:
        """Registra dano sofrido pelo protagonista durante a cena corrente."""
        dados = self.carregar()
        recursos = dados.setdefault("recursos_gastos_neste_capitulo", {})
        recursos["dano_sofrido"] = recursos.get("dano_sofrido", 0) + pontos_dano
        self.salvar(dados)

    def registrar_item_obtido(self, item_nome: str, quantidade: int = 1, tipo: str = "geral") -> None:
        """Registra novo item adquirido na cena corrente."""
        dados = self.carregar()
        obtidos = dados.setdefault("recursos_gastos_neste_capitulo", {}).setdefault("itens_obtidos", [])
        obtidos.append({"item": item_nome, "quantidade": quantidade, "tipo": tipo})
        self.salvar(dados)

    def exibir_painel_volatil(self) -> None:
        """Imprime o estado atual da memória volátil de forma legível."""
        dados = self.carregar()
        print("\n=======================================================")
        print("🧠 BUFFER DE MEMÓRIA VOLÁTIL (CENA EM ANDAMENTO)")
        print("=======================================================")
        print(f"📖 Capítulo: {dados.get('capitulo_em_andamento')} | Estágio: {dados.get('estagio_cena_atual')}")
        print(f"⚡ Tensão: {dados.get('tensao_calibrada')} | Local: {dados.get('localizacao_cena')}")
        print(f"🎲 Semente Ativa: {dados.get('oraculo_ativo_cena', {}).get('foco_ou_semente')}")
        print(f"🌪️ Reviravolta: {dados.get('oraculo_ativo_cena', {}).get('reviravolta_prevista')}")
        print(f"👤 NPC Destaque: {dados.get('oraculo_ativo_cena', {}).get('npc_em_destaque')}")
        
        modificadores = dados.get("modificadores_temporarios", [])
        if modificadores:
            print("\n✨ Modificadores Temporários:")
            for m in modificadores:
                print(f"   - {m.get('nome')}: {m.get('efeito')} ({m.get('duracao_turnos')} turnos)")
                
        gastos = dados.get("recursos_gastos_neste_capitulo", {})
        print(f"\n📦 Recursos Gastos na Cena:")
        print(f"   - Dano Sofrido: {gastos.get('dano_sofrido', 0)} HP")
        if gastos.get("itens_consumidos"):
            print(f"   - Consumidos: {', '.join([f'{i[\"quantidade\"]}x {i[\"item\"]}' for i in gastos['itens_consumidos']])}")
        if gastos.get("itens_obtidos"):
            print(f"   - Obtidos: {', '.join([f'{i[\"quantidade\"]}x {i[\"item\"]}' for i in gastos['itens_obtidos']])}")
        print("=======================================================\n")

if __name__ == "__main__":
    buffer = BufferMemoriaVolatil()
    buffer.exibir_painel_volatil()
