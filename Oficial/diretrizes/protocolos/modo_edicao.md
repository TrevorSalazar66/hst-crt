# Protocolo: Modo Edição (`edicao`)

> **Propósito do Modo:** Permitir a **revisão cirúrgica, reescrita ou refinamento dramático de capítulos já existentes** (`saga/capitulo_XX.md`), assegurando que quaisquer alterações factuais (danos sofridos, itens gastos/obtidos, atitudes de NPCs ou revelações) sejam retroalimentadas com precisão no estado dinâmico (`background/dinamico/`) e na continuidade dos capítulos posteriores.

---

## 🎯 1. Tipos de Edição e Nível de Impacto

Ao receber uma solicitação de edição, classifique a alteração em uma das duas categorias:

| Categoria de Edição | Descrição | Impacto no Estado Dinâmico |
| :--- | :--- | :--- |
| **A) Estilística / Atmosférica** | Aumentar a tensão dos diálogos, aprofundar descrições sensoriais (*Show, Don't Tell*), ajustar o ritmo da prosa ou corrigir pontuação. | **Nenhum.** O estado JSON permanece idêntico; apenas o arquivo `.md` do capítulo é atualizado. |
| **B) Factual / Consequencial** | Inserir um novo ferimento, poupar/eliminar um NPC, gastar ou adquirir recursos, mudar a rota de fuga ou alterar uma pista descoberta. | **Crítico.** Exige atualização imediata dos arquivos em `background/dinamico/` e verificação de continuidade. |

---

## 🔄 2. Ciclo de Execução do Modo Edição

```
[ 1. Diagnóstico & Escopo ] ➔ [ 2. Mapeamento de Continuidade ] ➔ [ 3. Edição do Capítulo ] ➔ [ 4. Reconciliação do Estado ] ➔ [ 5. Relatório de Impacto ]
```

### Passo 1: Diagnóstico de Escopo e Localização

* Identifique o capítulo alvo (`saga/capitulo_XX.md`) e analise se ele é o **capítulo mais recente** ou um **capítulo anterior**.
* Leia o texto original do capítulo e o bloco final de `Consequências & Atualizações da Cena`.

### Passo 2: Mapeamento de Efeito Dominó (*Ripple Effect*)

Se o capítulo a ser editado for anterior ao capítulo atual (ex: editando o Capítulo 2 enquanto a história já está no Capítulo 5):

* Avalie se a mudança anula eventos ocorridos nos capítulos seguintes (ex: se o protagonista não perdeu a pistola no Cap 2, ele agora a possui nos Capítulos 3, 4 e 5).
* Se houver contradição grave, alerte o usuário antes de prosseguir ou proponha os ajustes correspondentes nos capítulos subsequentes e no `resumos/historico_resumido.md`.

### Passo 3: Aplicação da Edição no Arquivo (`saga/capitulo_XX.md`)

* Reescreva as seções necessárias mantendo a coesão com a voz narrativa e as metodologias de [construcao_cena.md](file:///c:/Users/João/Documents/Programas/Python/hrt-crt/Oficial/diretrizes/metodologias/construcao_cena.md).
* **Obrigatório:** Atualize o cabeçalho (caso o *Estado de Tensão* tenha mudado) e reescreva a seção final de **Consequências & Atualizações da Cena** com os novos dados de saúde, recursos e ganchos.

### Passo 4: Reconciliação do Estado Dinâmico (`background/dinamico/`)

Ajuste os arquivos JSON para refletir a nova realidade da cena:

* **`estado_personagens.json`:** Atualize a vitalidade, ferimentos específicos e lista de inventário/munição.
* **`estado_trama.json`:** Se a edição resolveu, cancelou ou criou novos ganchos, atualize os registros de *plot hooks*.
* **`estado_mundo.json`:** Atualize a reputação com facções ou o nível de alerta distrital caso a abordagem na cena tenha mudado (ex: de tiroteio barulhento para fuga furtiva).

### Passo 5: Atualização do Histórico e Confirmação

1. Se a alteração afetou pontos centrais da trama, sincronize o arquivo `resumos/historico_resumido.md`.
2. Apresente ao usuário um relatório conciso:
   * Trechos principais modificados.
   * Modificações realizadas no estado dinâmico (JSON).
   * Confirmação de integridade da linha do tempo.

---

## 📋 3. Formato do Relatório de Confirmação de Edição

```markdown
### ✍️ Edição Concluída: Capítulo [XX] — *[Título]*

* **Tipo de Alteração:** [Estilística / Factual]
* **Principais Mudanças no Texto:** [Resumo em 2 a 3 tópicos das alterações de cena]
* **Atualizações de Estado Dinâmico:**
  - `estado_personagens.json`: [Ex: Saúde ajustada para 65% / Adicionada bandagem ao inventário]
  - `estado_trama.json`: [Ex: Gancho #3 atualizado com nova pista]
* **Impacto na Continuidade:** [Nenhum conflito detectado / Histórico resumido sincronizado]
```

---

## ⚖️ 4. Regras de Integridade do Modo Edição

1. **Não Alterar o Progresso da Saga:** O Modo Edição **não incrementa** o `capitulo_atual` em `config/config_geral.json`.
2. **Preservação de Estilo:** A prosa editada deve manter o mesmo rigor estilístico (*Show, Don't Tell*, ancoragem sensorial e diálogos com subtexto).
3. **Consistência Atômica:** Nunca modifique um fato no texto sem atualizar simultaneamente o bloco de consequências no rodapé do arquivo `.md` e os arquivos `.json` de estado.
