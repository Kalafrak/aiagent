import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory. Creates parent directories if they do not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    parent = os.path.dirname(abs_target)
    if not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)

    try:
        with open(abs_target, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {e}'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
