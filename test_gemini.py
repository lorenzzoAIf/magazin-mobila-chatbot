import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-flash-latest")
raspuns = model.generate_content("Salut, poti sa te prezinti pe scurt?")
print(raspuns.text)
