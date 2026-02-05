from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME


client = OpenAI(api_key=OPENAI_API_KEY)


def parse_and_screen_resume(resume_text: str, role: str = "Not specified") -> str:
    """
    Extract candidate details and screen resume using ONLY resume content.
    """

    prompt = f"""
You are an AI-powered Applicant Tracking System.

Resume Text:
{resume_text}

Tasks:
1. Extract the following details if present:
   - Full Name
   - Email Address
   - Phone Number
   - Total Experience (in years, if possible)
   - Key Skills / Technologies
   - Notable Projects or Work Experience

2. If any field is missing, explicitly say "Not found in resume".

3. Based ONLY on the resume content, assess suitability for the role: {role}

4. Provide a clear screening verdict:
   - Good Fit
   - Partial Fit
   - Not a Fit

Rules:
- Use ONLY resume information
- Do NOT assume or invent details
- Keep output structured and professional
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert recruitment screening system."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
