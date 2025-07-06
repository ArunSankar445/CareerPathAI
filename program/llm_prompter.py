import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")


def load_prompt(template_path):
    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()


def get_completion(prompt):
    """
    Send prompt to Gemini and get text response.
    """
    response = model.generate_content(prompt)
    return response.text.strip()
