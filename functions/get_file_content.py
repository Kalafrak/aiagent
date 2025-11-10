import os
from config import *

def get_file_content(working_directory, file_path):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(abs_target) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
    except Exception as e:
        return f'Error: {e}'
    
    if len(file_content_string) < MAX_CHARS:
        return file_content_string
    if len(file_content_string) == MAX_CHARS:
        return f'{file_content_string}[...File "{file_path}" truncated at {MAX_CHARS} characters]'
