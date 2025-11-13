import os
import sys
from config import *

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

from dotenv import dotenv_values

api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)



def main():
    args = sys.argv
    messages = [
        types.Content(role="user", parts=[types.Part(text=args[1])]),
    ]
    if len(args) < 2:
        sys.exit("Error: No prompt given!")
    response = client.models.generate_content(
        model=model_name, 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    print(f"{response.text}")
    if "--verbose" in args:
        print(f"User prompt: {args[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
