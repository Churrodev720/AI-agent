# from subdirectory.filename import function_name
from functions.functinsfile import run_python_file


f = run_python_file("calculator", "main.py")
print(f)

f = run_python_file("calculator", "main.py", ["3 + 5"])
print(f)

f = run_python_file("calculator", "tests.py")
print(f)

f = run_python_file("calculator", "../main.py") #should return errorS
print(f)

f = run_python_file("calculator", "nonexistent.py") #should return error
print(f)