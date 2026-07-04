print("USING GEMINI AI.PY")

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_company(text: str):

    print("Gemini received text")

    prompt = f"""
You are a senior business analyst.

Analyze the following company data and return:

1. Company Summary
   (2-3 paragraphs)
2. Industry
3. Products/Services
4. Business Model
5. Target Customers
6. Strengths
   - Point 1
   - Point 2
   - Point 3
7. Weaknesses
   - Point 1
   - Point 2
8. Competitors
   - Competitor 1
   - Competitor 2
   - Competitor 3
9. Key Insights
   - Point 1
   - Point 2
   - Point 3

Website Content:
{text}

Keep the total response under 500 words.
"""
    
    print("Calling Gemini...")

    response = model.generate_content(prompt)
    
    print("Gemini responded")
    
    return response.text