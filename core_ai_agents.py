import sys

from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose_flag = False
    if len(sys.argv) < 2:
        print("Please enter a prompt, or try 'Hey Agent, I want to learn something cool!'")
        sys.exit(1)
    elif len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    prompt = sys.argv[1]

    # types.Content represents one message in the conversation.
    # types.Part represents actual content chunk to be sent. In this scenario, the prompt from CLI is the content part.
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    # we pass messages as content because it is the chat history.
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=messages
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        print("Bad Response")
        return

    if verbose_flag:
        print(f"User prompt: {prompt}")
        print(f"Request tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()