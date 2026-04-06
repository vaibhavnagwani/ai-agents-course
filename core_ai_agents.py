from dotenv import load_dotenv
import os
from google import genai
from openai import api_key

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents='''Hi Gemini! I hope you're having a good time!'''
    )

    print(response)
    if response is None or response.usage_metadata is None:
        return
    print(f"Request tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()