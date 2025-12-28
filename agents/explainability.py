import os
import google.generativeai as genai
import json

def explain_findings(text: str, technical_findings: dict) -> dict:
    """
    Translates technical findings into plain language for managers.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY not found"}

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Convert findings to string to pass to context
    findings_str = json.dumps(technical_findings, ensure_ascii=False)

    prompt = f"""
    Você é um Agente de Explicabilidade (ExplainabilityAgent), focado em comunicação clara para gestores públicos e cidadãos.
    
    Com base no TEXTO ORIGINAL do documento e nos ACHADOS TÉCNICOS dos outros agentes, gere uma explicação didática.
    
    ACHADOS TÉCNICOS:
    {findings_str}

    TEXTO ORIGINAL (AMOSTRA):
    {text[:10000]}

    Seu objetivo:
    1. Traduzir o 'economês' para português claro.
    2. Explicar o impacto prático dos riscos e problemas encontrados.
    3. Sugerir ações corretivas de alto nível.

    Responda APENAS em formato JSON:
    {{
        "resumo_executivo": "Texto corrido, amigável, resumindo a situação.",
        "pontos_atencao_cidadao": ["Ponto 1 simplificado", "Ponto 2 simplificado"],
        "recomendacoes_gestor": ["Ação 1", "Ação 2"]
    }}
    """

    try:
        response = model.generate_content(prompt)
        content = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        return {
            "error": f"Error in ExplainabilityAgent: {str(e)}", 
            "resumo_executivo": "Não foi possível gerar a explicação.",
            "pontos_atencao_cidadao": [], 
            "recomendacoes_gestor": []
        }
