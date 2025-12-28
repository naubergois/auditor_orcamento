![Auditor Orçamento Banner](banner.png)

# 🛡️ Auditor de Orçamento com IA Generativa (SOF)

Este projeto apresenta uma plataforma funcional de auditoria de documentos orçamentários (LOA, LDO, Notas Técnicas) utilizando **Agentes de Inteligência Artificial** (Google Gemini).

O objetivo é aumentar a **transparência**, a **eficiência do gasto público** e empoderar auditores e cidadãos com uma ferramenta capaz de "ler" e analisar documentos complexos em segundos.

---

## 🏗️ Arquitetura

O sistema utiliza uma arquitetura de múltiplos agentes, orquestrada para simular uma equipe de auditoria:

1.  **AuditorAgent**: Focado em identificar riscos fiscais e contas que não fecham.
2.  **ComplianceAgent**: Verifica a aderência à LRF (Lei de Responsabilidade Fiscal) e Constituição.
4.  **ExplainabilityAgent**: Traduz os achados técnicos (economês) para linguagem clara.

### Diagrama Visual
O fluxo de trabalho foi desenhado para evitar alucinações de IA e garantir consistência:

1.  **Orchestrator**: Recebe o texto e decide quais agentes acionar.
2.  **Agentes Paralelos**: Auditoria, Compliance e Consistência rodam simultaneamente para performance.
3.  **Explainability**: Consolida os resultados técnicos em linguagem natural.

### Detalhamento Técnico
- **Frontend**: Streamlit (Python) - Interface limpa e reativa.
- **Backend AI**: Agentes autônomos consumindo Google Gemini 2.0 via API.
- **Arquitetura**: Micro-agentes independentes, cada um com *prompts* especializados (System Instructions).

![Arquitetura](architecture_didactic.png)

## 🚀 Como Rodar Localmente

### Pré-requisitos
- Python 3.9+
- Uma chave de API do Google Gemini (`GEMINI_API_KEY`)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/auditor_orcamento.git
cd auditor_orcamento
```

2. Crie um ambiente virtual (recomendado):
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure a chave da API:
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione a linha: `GEMINI_API_KEY=sua_chave_aqui`
   - Ou exporte no terminal: `export GEMINI_API_KEY=sua_chave_aqui`

   **Alternativa (Streamlit Secrets):**
   - Crie um arquivo `.streamlit/secrets.toml` com o conteúdo:
     ```toml
     GEMINI_API_KEY = "sua_chave_aqui"
     ```

5. Gere o PDF de exemplo (Opcional):
```bash
python3 examples/generate_mock.py
```

6. Execute o aplicativo:
```bash
streamlit run app.py
```

## ☁️ Como Deployar no Streamlit Cloud (Recomendado para Banca)

1. Suba este código para o **GitHub**.
2. Crie uma conta no [Streamlit Cloud](https://streamlit.io/cloud).
3. Conecte seu GitHub e selecione o repositório.
4. Antes de clicar em "Deploy", vá em **Advanced Settings** -> **Secrets**.
5. Adicione sua chave lá:
   ```toml
   GEMINI_API_KEY = "sua_chave_do_google_aqui"
   ```
6. Clique em **Deploy**. O app estará online em minutos!

## 🖥️ Como Usar

1. Acesse `http://localhost:8501`.
2. Na barra lateral, escolha entre fazer **Upload** de um PDF seu ou usar o **Exemplo (Mock)**.
3. Clique em **"Carregar Exemplo"** (se escolheu o mock).
4. Clique no botão **"Executar Auditoria Inteligente"**.
5. Aguarde a análise e explore as abas de resultados.

## 🎥 Vídeo de Demonstração

Assista ao vídeo mostrando o uso da ferramenta: [Baixar/Assistir Vídeo (MP4)](https://github.com/naubergois/auditor_orcamento/raw/main/Comousar.mp4)

## ⚠️ Limitações do Protótipo

- Esta versão é uma demonstração (MVP) focada na arquitetura de agentes.
- A análise depende da qualidade da extração de texto do PDF.
- A precisão das análises legais depende do contexto fornecido ao modelo (prompt engineering).
- Para uso em produção, recomenda-se fina sintonia (RAG - Retrieval Augmented Generation) com a base completa de leis.
