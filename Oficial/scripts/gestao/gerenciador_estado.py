import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class GerenciadorEstado:
    """Gerencia leitura, escrita e consolidação de todos os estados dinâmicos e memória volátil."""

    def __init__(self, pasta_dinamico: Optional[str] = None):
        if pasta_dinamico:
            self.pasta_dinamico = Path(pasta_dinamico)
        else:
            self.pasta_dinamico = Path(__file__).resolve().parent.parent.parent / "background" / "dinamico"

    def ler_estado(self, nome_arquivo: str) -> Dict[str, Any]:
        """Carrega um arquivo JSON da pasta dinamica."""
        caminho = self.pasta_dinamico / nome_arquivo
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo de estado não encontrado: {caminho}")
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def salvar_estado(self, nome_arquivo: str, dados: Dict[str, Any]) -> None:
        """Grava dados no arquivo JSON da pasta dinamica."""
        caminho = self.pasta_dinamico / nome_arquivo
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    # -------------------------------------------------------------------------
    # Métodos do Protagonista & Personagens
    # -------------------------------------------------------------------------

    def aplicar_dano_saude(self, dano: int, ferimento_desc: Optional[str] = None) -> int:
        """Aplica dano à saúde do protagonista e adiciona ferimento se especificado."""
        personagens = self.ler_estado("estado_personagens.json")
        protagonista = personagens.setdefault("protagonista", {})
        saude_atual = protagonista.get("saude", 100)
        nova_saude = max(0, min(100, saude_atual - dano))
        protagonista["saude"] = nova_saude
        
        if nova_saude <= 0:
            protagonista["condicao_fisica"] = "Incapacitado / Risco de Morte"
        elif nova_saude < 40:
            protagonista["condicao_fisica"] = "Gravemente Ferido"
        elif nova_saude < 75:
            protagonista["condicao_fisica"] = "Ferido"
        else:
            protagonista["condicao_fisica"] = "Saudável"
            
        if ferimento_desc:
            protagonista.setdefault("ferimentos_ativos", []).append(ferimento_desc)
            
        self.salvar_estado("estado_personagens.json", personagens)
        return nova_saude

    def curar_saude(self, cura: int, remover_ferimento: Optional[str] = None) -> int:
        """Restaura pontos de saúde do protagonista."""
        personagens = self.ler_estado("estado_personagens.json")
        protagonista = personagens.setdefault("protagonista", {})
        saude_atual = protagonista.get("saude", 100)
        nova_saude = min(100, saude_atual + cura)
        protagonista["saude"] = nova_saude
        
        if remover_ferimento and "ferimentos_ativos" in protagonista:
            if remover_ferimento in protagonista["ferimentos_ativos"]:
                protagonista["ferimentos_ativos"].remove(remover_ferimento)
                
        self.salvar_estado("estado_personagens.json", personagens)
        return nova_saude

    def adicionar_item_inventario(self, nome_item: str, quantidade: int = 1, tipo: str = "geral") -> None:
        """Adiciona ou incrementa um item no inventário do protagonista."""
        personagens = self.ler_estado("estado_personagens.json")
        inventario = personagens.setdefault("protagonista", {}).setdefault("inventario", [])
        
        encontrado = False
        for item_obj in inventario:
            if isinstance(item_obj, dict) and item_obj.get("item", "").lower() == nome_item.lower():
                item_obj["quantidade"] = item_obj.get("quantidade", 1) + quantidade
                encontrado = True
                break
                
        if not encontrado:
            inventario.append({
                "item": nome_item,
                "quantidade": quantidade,
                "tipo": tipo
            })
            
        self.salvar_estado("estado_personagens.json", personagens)

    def consumir_item_inventario(self, nome_item: str, quantidade: int = 1) -> bool:
        """Consome uma quantidade de item do inventário."""
        personagens = self.ler_estado("estado_personagens.json")
        inventario = personagens.setdefault("protagonista", {}).setdefault("inventario", [])
        
        for item_obj in inventario:
            if isinstance(item_obj, dict) and item_obj.get("item", "").lower() == nome_item.lower():
                qtd_atual = item_obj.get("quantidade", 1)
                if qtd_atual >= quantidade:
                    item_obj["quantidade"] = qtd_atual - quantidade
                    if item_obj["quantidade"] <= 0:
                        inventario.remove(item_obj)
                    self.salvar_estado("estado_personagens.json", personagens)
                    return True
                else:
                    return False
        return False

    # -------------------------------------------------------------------------
    # Métodos da Trama e Ganchos
    # -------------------------------------------------------------------------

    def adicionar_gancho(self, descricao: str, prioridade: str = "Media", id_gancho: Optional[str] = None) -> str:
        """Registra um novo gancho de enredo ativo."""
        trama = self.ler_estado("estado_trama.json")
        ganchos = trama.setdefault("ganchos_abertos", [])
        capitulo_atual = trama.get("capitulo_atual_num", 1)
        
        if not id_gancho:
            id_gancho = f"gancho_{len(ganchos) + 1:02d}"
            
        novo_gancho = {
            "id": id_gancho,
            "descricao": descricao,
            "prioridade": prioridade,
            "capitulo_origem": capitulo_atual,
            "status": "ativo"
        }
        ganchos.append(novo_gancho)
        self.salvar_estado("estado_trama.json", trama)
        return id_gancho

    def atualizar_status_gancho(self, id_gancho: str, novo_status: str) -> bool:
        """Atualiza status de um gancho (ativo, em_progresso, resolvido, fracassado)."""
        trama = self.ler_estado("estado_trama.json")
        ganchos = trama.setdefault("ganchos_abertos", [])
        for g in ganchos:
            if isinstance(g, dict) and g.get("id") == id_gancho:
                g["status"] = novo_status
                self.salvar_estado("estado_trama.json", trama)
                return True
        return False

    # -------------------------------------------------------------------------
    # Métodos do Mundo e Relógios de Urgência
    # -------------------------------------------------------------------------

    def adicionar_relogio_urgencia(self, nome: str, turnos_max: int, consequencia: str) -> None:
        """Cria um relógio de contagem regressiva (Ticking Clock)."""
        mundo = self.ler_estado("estado_mundo.json")
        relogios = mundo.setdefault("relogs_urgencia", mundo.setdefault("relogios_urgencia", []))
        relogios.append({
            "nome": nome,
            "turnos_restantes": turnos_max,
            "consequencia_ao_zerar": consequencia
        })
        self.salvar_estado("estado_mundo.json", mundo)

    def avancar_relogios_urgencia(self, decremento: int = 1) -> List[str]:
        """Avança todos os relógios ativos e retorna aqueles que foram engatilhados/zerados."""
        mundo = self.ler_estado("estado_mundo.json")
        relogios = mundo.get("relogios_urgencia", [])
        alertas_disparados = []
        
        for r in relogios:
            r["turnos_restantes"] = max(0, r.get("turnos_restantes", 1) - decremento)
            if r["turnos_restantes"] == 0:
                alertas_disparados.append(f"⏰ RELÓGIO ENGATILHADO: [{r['nome']}] — Consequência: {r['consequencia_ao_zerar']}")
                
        self.salvar_estado("estado_mundo.json", mundo)
        return alertas_disparados

    # -------------------------------------------------------------------------
    # Consolidação de Fim de Capítulo
    # -------------------------------------------------------------------------

    def consolidar_fim_de_capitulo(self, titulo_capitulo: str, resumo_breve: str) -> None:
        """Consolida os dados da memória volátil no histórico definitivo e avança o capítulo."""
        trama = self.ler_estado("estado_trama.json")
        capitulo_num = trama.get("capitulo_atual_num", 1)
        
        # Registra no histórico
        historico = trama.setdefault("historico_capitulos", [])
        historico.append({
            "capitulo": capitulo_num,
            "titulo": titulo_capitulo,
            "resumo": resumo_breve
        })
        
        # Avança capítulo
        trama["capitulo_atual_num"] = capitulo_num + 1
        self.salvar_estado("estado_trama.json", trama)
        
        # Avança relógios de urgência
        self.avancar_relogios_urgencia(1)
        
        # Reseta memória volátil para o próximo capítulo
        try:
            from memoria_volatil import BufferMemoriaVolatil
            buffer = BufferMemoriaVolatil(str(self.pasta_dinamico))
            buffer.resetar_buffer(capitulo_num + 1)
        except Exception:
            pass

    # -------------------------------------------------------------------------
    # Painel de Status Geral
    # -------------------------------------------------------------------------

    def exibir_status_geral(self) -> None:
        """Exibe o painel visual completo do estado do universo."""
        mundo = self.ler_estado("estado_mundo.json")
        personagens = self.ler_estado("estado_personagens.json")
        trama = self.ler_estado("estado_trama.json")
        protagonista = personagens.get("protagonista", {})

        print("\n=======================================================")
        print("🗺️ STATUS ATUAL DO UNIVERSO NARRATIVO")
        print("=======================================================")
        print(f"📖 Capítulo Atual: {trama.get('capitulo_atual_num')} | Arco: {trama.get('arco_narrativo_atual')}")
        print(f"📍 Localização: {mundo.get('localizacao_atual')} ({mundo.get('distrito_ou_regiao', 'Região N/A')})")
        
        clima = mundo.get("condicao_climatica", {})
        if isinstance(clima, dict):
            print(f"🌦️ Clima: {clima.get('clima')} | Temp: {clima.get('temperatura')} | Ar: {clima.get('toxidade_ar')}")
        else:
            print(f"🌦️ Clima: {clima}")
            
        print(f"🚨 Nível de Alerta Geral: {mundo.get('nivel_alerta_geral', 'Baixo')}")
        
        print("\n👤 PROTAGONISTA:")
        print(f"   ❤️ Saúde: {protagonista.get('saude')}% ({protagonista.get('condicao_fisica', 'Normal')})")
        print(f"   🧠 Estresse/Sanidade: {protagonista.get('sanidade_ou_estresse', 0)}%")
        
        ferimentos = protagonista.get("ferimentos_ativos", [])
        if ferimentos:
            print(f"   🩹 Ferimentos Ativos: {', '.join(ferimentos)}")
            
        inventario = protagonista.get("inventario", [])
        if inventario:
            itens_str = []
            for item in inventario:
                if isinstance(item, dict):
                    itens_str.append(f"{item.get('quantidade', 1)}x {item.get('item')}")
                else:
                    itens_str.append(str(item))
            print(f"   🎒 Inventário: {', '.join(itens_str)}")
        else:
            print("   🎒 Inventário: (Vazio)")

        ganchos = trama.get("ganchos_abertos", [])
        ativos = [g for g in ganchos if isinstance(g, dict) and g.get("status") in ["ativo", "em_progresso"]]
        print(f"\n⚓ GANCHOS DE ENREDO ATIVOS ({len(ativos)}):")
        for g in ativos:
            print(f"   [{g.get('prioridade', 'Media')}] {g.get('id')}: {g.get('descricao')}")
            
        relogios = mundo.get("relogios_urgencia", [])
        if relogios:
            print("\n⏰ RELÓGIOS DE URGÊNCIA (TICKING CLOCKS):")
            for r in relogios:
                print(f"   - {r.get('nome')}: {r.get('turnos_restantes')} turnos restantes")
                
        print("=======================================================\n")

if __name__ == "__main__":
    caminho_script = Path(__file__).resolve().parent
    pasta_dinamico = caminho_script.parent.parent / "background" / "dinamico"
    gerenciador = GerenciadorEstado(str(pasta_dinamico))
    gerenciador.exibir_status_geral()
