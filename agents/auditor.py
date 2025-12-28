import os
import google.generativeai as genai
import json

def analyze_risks(text: str) -> dict:
    """
    Analyzes the budget text for financial risks and improprieties.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY not found"}

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    Você é um Auditor Especialista em Orçamento Público (AuditorAgent).
    Analise o texto abaixo, extraído de um documento orçamentário (LOA, LDO, Nota Técnica).
    
    Seu objetivo é identificar:
    1. Riscos fiscais ou orçamentários.
    2. Indícios de impropriedade ou má gestão.
    3. Pontos que merecem atenção especial da fiscalização.

    Responda APENAS em formato JSON, com a seguinte estrutura:
    {{
        "riscos": [
            {{
                "titulo": "Título curto do risco",
                "gravidade": "ALTA" | "MÉDIA" | "BAIXA",
                "descricao": "Explicação técnica detalhada"
            }}
        ],
        "parecer_geral": "Resumo executivo da análise de riscos."
    }}

    Se não encontrar nada relevante, retorne listas vazias, mas sempre no formato JSON válido.
    
    TEXTO PARA ANÁLISE:
    {text[:30000]}  # Limiting context window just in case
    """

    try:
        response = model.generate_content(prompt)
        # Clean up code fences if present
        content = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        return {"error": f"Error in AuditorAgent: {str(e)}", "riscos": [], "parecer_geral": "Erro na análise."}
