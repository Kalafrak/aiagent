# python
def show(title, wd, dir_):
    from functions.get_files_info import get_files_info
    print(title)
    result = get_files_info(wd, dir_)
    print(" " + result.replace("\n", "\n "))

if __name__ == "__main__":
    show("Result for current directory:", "calculator", ".")
    show("\nResult for 'pkg' directory:", "calculator", "pkg")
    show("\nResult for '/bin' directory:", "calculator", "/bin")
    show("\nResult for '../' directory:", "calculator", "../")