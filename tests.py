# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info
f = get_files_info("calculator", ".")
print(f)
f = get_files_info("calculator", "pkg") 
print(f)
f = get_files_info("calculator", "/bin")
print(f)
f = get_files_info("calculator", "../")
print(f)