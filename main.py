import os
import sys
from config import *
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_function import call_function

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

from dotenv import dotenv_values

api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
    ]
)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model=model_name, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        )
    )

    for candidate in response.candidates:
        messages.append(candidate.content)

    if not response.function_calls and response.text:
        return response.text
    else:
        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose=verbose)
            part = function_call_result.parts[0]
            function_responses.append(part)
        
        messages.append(types.Content(role="user", parts=function_responses))
        return None
    



def main():
    args = sys.argv
    messages = [
        types.Content(role="user", parts=[types.Part(text=args[1])]),
    ]
    if len(args) < 2:
        sys.exit("Error: No prompt given!")
    
    verbose = "--verbose" in args

    iters = 0
    while iters < MAX_ITERS:
        iters += 1

        final_text = generate_content(client, messages, verbose)

        if final_text:
            print("Final response:")
            print(final_text)
            break
    
if __name__ == "__main__":
    main()
