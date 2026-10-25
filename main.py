
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the local .env file
load_dotenv()

def get_groq_api_key():
    api_key = os.getenv("GROQ_API_KEY")

    if api_key:
        return api_key

    try:
        import streamlit as st
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return None



def generate_draft(user_request: str) -> str:
    """Generate the first draft based on the user's request."""

    api_key = get_groq_api_key()

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful writing assistant. "
                    "Generate a clear and professional first draft. "
                    "Do not invent names, dates, or personal details."
                )
            },
            {
                "role": "user",
                "content": user_request
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


def improve_draft(original_draft: str, feedback: str) -> str:
    """Revise the draft using feedback provided by a human."""

    if not original_draft.strip():
        raise ValueError("The original draft cannot be empty.")

    if not feedback.strip():
        raise ValueError("Please provide feedback before improving the draft.")

    api_key = get_groq_api_key()

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a writing assistant that improves drafts "
                    "using human feedback. Follow the feedback carefully. "
                    "Preserve the original meaning unless asked to change it. "
                    "Do not invent facts. Return only the revised draft."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Original draft:\n{original_draft}\n\n"
                    f"Human feedback:\n{feedback}\n\n"
                    "Improve the draft according to this feedback."
                )
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
