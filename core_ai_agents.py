import sys

from dotenv import load_dotenv
import os
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("Please enter a prompt, or try 'Hey Agent, I want to learn something cool!'")
        sys.exit(1)

    prompt = sys.argv[1]

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        return
    print(f"Request tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()