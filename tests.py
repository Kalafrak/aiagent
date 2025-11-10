# python
from functions.get_file_content import get_file_content

def show_case(wd, path):
    result = get_file_content(wd, path)
    # keep output concise so it’s readable
    snippet = result if result.startswith("Error:") else result.splitlines()[0]
    print(f"{path}: {snippet}")

if __name__ == "__main__":
    print("Running file content checks:")
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))