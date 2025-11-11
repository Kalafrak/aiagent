# python
from functions.write_file import write_file

def show_case(wd, path, content):
    result = write_file(wd, path, content)
    # keep output concise so it’s readable
    snippet = result if result.startswith("Error:") else result.splitlines()[0]
    print(f"{path}: {snippet}")

if __name__ == "__main__":
    print("Write_file checks:")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
