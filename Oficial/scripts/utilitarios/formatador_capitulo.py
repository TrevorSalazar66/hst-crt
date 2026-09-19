def formatar_cabecalho_capitulo(numero_capitulo: int, titulo: str, premissa_oraculo: dict) -> str:
    """Gera o cabeçalho formatado em Markdown para os capítulos."""
    cabecalho = f"""# Capítulo {numero_capitulo:02d}: {titulo}

> **Oráculo de Cena**: {premissa_oraculo.get('foco_cena', 'N/A')}  
> **Reviravolta**: {premissa_oraculo.get('reviravolta', 'N/A')}  
> **Atitude NPC**: {premissa_oraculo.get('atitude_npc', 'N/A')}

---

"""
    return cabecalho
