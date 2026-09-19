import json
import sys
from pathlib import Path
from typing import Dict, Any

class GerenciadorEstado:
    """Carrega, lê e salva o estado mutável do universo em background/dinamico/."""

    def __init__(self, pasta_dinamico: str = "background/dinamico"):
        self.pasta_dinamico = Path(pasta_dinamico)

    def ler_estado(self, nome_arquivo: str) -> Dict[str, Any]:
        caminho = self.pasta_dinamico / nome_arquivo
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo de estado não encontrado: {caminho}")
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def salvar_estado(self, nome_arquivo: str, dados: Dict[str, Any]) -> None:
        caminho = self.pasta_dinamico / nome_arquivo
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    def exibir_status_geral(self) -> None:
        print("\n--- STATUS ATUAL DO UNIVERSO ---")
        mundo = self.ler_estado("estado_mundo.json")
        personagens = self.ler_estado("estado_personagens.json")
        trama = self.ler_estado("estado_trama.json")

        print(f"📍 Localização: {mundo.get('localizacao_atual')}")
        print(f"🌦️ Clima: {mundo.get('condicao_climatica')}")
        print(f"📖 Capítulo Atual: {trama.get('capitulo_atual_num')}")
        print(f"👤 Protagonista Saúde: {personagens.get('protagonista', {}).get('saude')}%")
        print(f"🎒 Inventário: {', '.join(personagens.get('protagonista', {}).get('inventario', []))}")
        print(f"⚓ Ganchos Abertos: {len(trama.get('ganchos_abertos', []))}")
        print("--------------------------------\n")

if __name__ == "__main__":
    caminho_script = Path(__file__).parent
    pasta_dinamico = caminho_script.parent.parent / "background" / "dinamico"
    gerenciador = GerenciadorEstado(str(pasta_dinamico))
    if "--status" in sys.argv or len(sys.argv) == 1:
        gerenciador.exibir_status_geral()
