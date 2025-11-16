from google import genai
from google.genai import types

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    functions = {"get_files_info": get_files_info, "get_file_content": get_file_content, "run_python_file": run_python_file, "write_file": write_file}
    args = dict(function_call_part.args or {})
    args["working_directory"] = "./calculator"
    function_name = function_call_part.name
    fn = functions.get(function_name)
    
    if fn == None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    else:
        result = fn(**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": result},
                )
            ],
        )