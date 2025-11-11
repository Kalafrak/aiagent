import os

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
