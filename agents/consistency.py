import os
import google.generativeai as genai
import json

def check_consistency(text: str) -> dict:
    """
    Checks for logical and numerical inconsistencies.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY not found"}

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    Você é um Agente de Consistência de Dados (ConsistencyAgent).
    Analise o texto buscando contradições, erros de cálculo óbvios ou incoerências lógicas entre diferentes seções.

    Exemplo: O texto diz que a receita cresceu, mas os gráficos mostram queda; ou soma das despesas não bate com o total.

    Responda APENAS em formato JSON:
    {{
        "inconsistencias": [
            {{
                "tipo": "NUMÉRICA" | "LÓGICA" | "TEXTUAL",
                "descricao": "Explique a contradição encontrada",
                "trecho_referencia": "Trecho aproximado onde ocorre"
            }}
        ],
        "analise_consistencia": "Parecer sobre a qualidade dos dados."
    }}

    TEXTO:
    {text[:30000]}
    """

    try:
        response = model.generate_content(prompt)
        content = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        return {"error": f"Error in ConsistencyAgent: {str(e)}", "inconsistencias": [], "analise_consistencia": "Erro"}
