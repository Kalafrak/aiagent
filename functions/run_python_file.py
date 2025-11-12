import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_target):
        return f'File "{file_path}" not found.'

    if not abs_target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(["python", file_path, *args], capture_output=True, cwd=abs_work, timeout=30, text=True)
        if completed_process.stdout == "" and completed_process.stderr == "":
            return "No output produced."
        completed_string = f'STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr}'
        if completed_process.returncode != 0:
            return completed_string + f" Process exited with code {completed_process.returncode}"
        return completed_string
    except Exception as e:
        return f'Error: executing Python file: {e}'