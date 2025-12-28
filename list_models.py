import google.generativeai as genai
import os
import toml

if not os.environ.get("GEMINI_API_KEY"):
    try:
        secrets = toml.load(".streamlit/secrets.toml")
        os.environ["GEMINI_API_KEY"] = secrets.get("GEMINI_API_KEY")
    except: pass

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

print("Listando modelos disponíveis:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
