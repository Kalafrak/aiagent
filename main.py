import os
import sys

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

from dotenv import dotenv_values

api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)



def main():
    args = sys.argv
    if len(args) < 2:
        sys.exit("Error: No prompt given!")
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=args[1])
    print(f"{response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
