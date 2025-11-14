import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))
    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(abs_target) == False:
        return f'Error: "{directory}"" is not a directory'
    try:
        dir_list = os.listdir(abs_target)
    except Exception as e:
        return f'Error: {e}'
    lines = []
    for name in dir_list:
        child = os.path.join(abs_target, name)
        try:
            size = os.path.getsize(child)
            is_dir = os.path.isdir(child)
        except Exception as e:
            return f'Error: {e}'
        lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

    return "\n".join(lines)