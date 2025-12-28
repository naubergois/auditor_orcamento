import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from orchestrator import AuditorOrchestrator
from utils.pdf_loader import extract_text_from_pdf

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="Auditor Orçamento - SOF",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Try to get key from secrets (Streamlit Cloud) or environment
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Custom CSS for "Premium" feel
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1f77b4;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 5px;
        height: 3em;
        width: 100%;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Auditor Orçamento 🤖")
st.sidebar.info("Solução de IA para o 14º Prêmio SOF.")
st.sidebar.markdown("---")

# Mock PDF Selection
st.sidebar.subheader("📄 Seleção de Arquivo")
upload_option = st.sidebar.radio("Fonte do documento:", ["Upload PDF", "Usar Exemplo (Mock)"])

if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = None

if upload_option == "Upload PDF":
    uploaded_file = st.sidebar.file_uploader("Carregar PDF", type=["pdf"])
    if uploaded_file is not None:
        st.session_state.pdf_content = uploaded_file.read()
else:
    if st.sidebar.button("Carregar Exemplo"):
        example_path = "examples/exemplo_orcamento.pdf"
        if os.path.exists(example_path):
            with open(example_path, "rb") as f:
                st.session_state.pdf_content = f.read()
            st.sidebar.success("Exemplo carregado!")
        else:
            st.sidebar.error("Arquivo de exemplo não encontrado.")

# Main Content
st.title("🛡️ Plataforma de Auditoria Inteligente")
st.markdown("""
Esta ferramenta utiliza **Agentes de Inteligência Artificial** para analisar leis orçamentárias (LOA/LDO), 
identificando **riscos**, **inconsistências** e verificando a **conformidade** com a LRF e a Constituição.
""")

if st.session_state.pdf_content:
    # If it's bytes (from mock), wrap it in BytesIO is not needed for pypdf sometimes, 
    # but let's handle both file_uploader object and raw bytes.
    import io
    file_obj = io.BytesIO(st.session_state.pdf_content)

    with st.expander("📝 Ver Texto Extraído", expanded=False):
        text = extract_text_from_pdf(file_obj)
        st.text_area("Texto cru", text, height=200)

    if st.button("🚀 Executar Auditoria Inteligente"):
        if not os.environ.get("GEMINI_API_KEY"):
            st.error("⚠️ GEMINI_API_KEY não configurada! Configure nas variáveis de ambiente.")
        else:
            with st.spinner("Os agentes estão analisando o documento..."):
                try:
                    orchestrator = AuditorOrchestrator()
                    results = orchestrator.run_audit(text)
                    
                    st.success("Análise Concluída!")
                    
                    # Tabs
                    tab1, tab2, tab3, tab4 = st.tabs([
                        "🚨 Riscos & Achados", 
                        "⚖️ Compliance (LRF)", 
                        "🔍 Consistência", 
                        "📢 Explicação Gestor"
                    ])

                    # 1. Auditor Findings
                    with tab1:
                        st.header("Achados do Auditor")
                        riscos = results['auditor'].get('riscos', [])
                        if riscos:
                            for idx, risco in enumerate(riscos):
                                with st.container():
                                    st.markdown(f"### {idx+1}. {risco.get('titulo', 'Risco')}")
                                    prioridade = risco.get('gravidade', 'BAIXA').upper()
                                    color = "red" if prioridade == "ALTA" else "orange" if prioridade == "MÉDIA" else "green"
                                    st.markdown(f"**Gravidade:** :{color}[{prioridade}]")
                                    st.write(risco.get('descricao', ''))
                                    st.divider()
                        else:
                            st.info("Nenhum risco crítico identificado.")
                        
                        st.subheader("Parecer Geral")
                        st.write(results['auditor'].get('parecer_geral', ''))

                    # 2. Compliance
                    with tab2:
                        st.header("Conformidade Legal (LRF/CF)")
                        items = results['compliance'].get('conformidade', [])
                        if items:
                            df_comp = pd.DataFrame(items)
                            st.table(df_comp)
                        else:
                            st.info("Nenhum item de conformidade retornado.")
                        
                        st.markdown(f"**Resumo:** {results['compliance'].get('resumo_compliance', '')}")

                    # 3. Consistency
                    with tab3:
                        st.header("Consistência de Dados")
                        incons = results['consistency'].get('inconsistencias', [])
                        for inc in incons:
                            st.warning(f"**{inc.get('tipo', 'ERRO')}**: {inc.get('descricao')}")
                            st.caption(f"Referência: {inc.get('trecho_referencia')}")

                    # 4. Explainability
                    with tab4:
                        expl = results['explainability']
                        st.header("Resumo para Gestores")
                        st.info(expl.get('resumo_executivo', ''))
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("Pontos de Atenção (Cidadão)")
                            for p in expl.get('pontos_atencao_cidadao', []):
                                st.write(f"• {p}")
                        
                        with col2:
                            st.subheader("Recomendações")
                            for r in expl.get('recomendacoes_gestor', []):
                                st.write(f"✅ {r}")

                except Exception as e:
                    st.error(f"Ocorreu um erro durante a execução: {str(e)}")

else:
    st.info("👈 Faça upload de um PDF ou use o exemplo na barra lateral para começar.")
