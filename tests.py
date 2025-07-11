# from subdirectory.filename import function_name
from functions.functinsfile import write_file


f = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f)

f = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f)

f = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f)