from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume(text, role):

    prompt = f"""
    Analyze this resume for {role} role.

    Give:
    1. ATS Score out of 100
    2. Missing Skills
    3. Strengths
    4. Weaknesses
    5. Suggestions
    6. Professional Summary

    Resume:
    {text}
    """

    try:

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"