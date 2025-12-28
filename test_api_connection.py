import os
import google.generativeai as genai
from dotenv import load_dotenv

# Try to load from .env
load_dotenv()

# Manually load from secrets.toml if env not set
if not os.environ.get("GEMINI_API_KEY"):
    try:
        import toml
        secrets = toml.load(".streamlit/secrets.toml")
        if "GEMINI_API_KEY" in secrets:
            os.environ["GEMINI_API_KEY"] = secrets["GEMINI_API_KEY"]
            print("Carregou chave do secrets.toml")
    except Exception as e:
        print(f"Erro ao ler secrets: {e}")

api_key = os.environ.get("GEMINI_API_KEY")
print(f"API Key encontrada: {api_key[:10]}...{api_key[-5:] if api_key else 'None'}")

if not api_key:
    print("❌ ERRO: Nenhuma API KEY encontrada.")
    exit(1)

genai.configure(api_key=api_key)

try:
    print("Tentando conectar ao Gemini...")
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content("Diga 'Olá, funcionou!' se você estiver me ouvindo.")
    print(f"✅ Sucesso! Resposta: {response.text}")
except Exception as e:
    print(f"❌ ERRO na chamada da API: {e}")
