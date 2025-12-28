import os
import google.generativeai as genai
import json

def verify_compliance(text: str) -> dict:
    """
    Verifies compliance with LRF (Lei de Responsabilidade Fiscal) and Constitution.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY not found"}

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    Você é um Especialista em Compliance Orçamentário (ComplianceAgent).
    Analise o texto abaixo verificando a aderência à LRF (Lei Complementar 101/2000) e Constituição Federal.

    Identifique:
    1. Menções a limites de gastos (pessoal, dívida).
    2. Cumprimento de metas fiscais (se citadas).
    3. Adequação legal geral.

    Responda APENAS em formato JSON:
    {{
        "conformidade": [
            {{
                "item": "Item analisado (ex: Limite de Pessoal)",
                "status": "CONFORME" | "NÃO CONFORME" | "ALERTA" | "NÃO IDENTIFICADO",
                "observacao": "Detalhe técnico"
            }}
        ],
        "resumo_compliance": "Visão geral da conformidade legal."
    }}

    TEXTO:
    {text[:30000]}
    """

    try:
        response = model.generate_content(prompt)
        content = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        return {"error": f"Error in ComplianceAgent: {str(e)}", "conformidade": [], "resumo_compliance": "Erro"}
