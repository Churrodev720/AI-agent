
from google import genai
from google.genai import types
from functions.functinsfile import run_python_file, write_file, get_file_content

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists content of specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="The file to get content from, relative to the working directory.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="The file which you run, relative to the working directory.",)
            ,
            "arguments": types.Schema(
                type=types.Type.ARRAY,
                description="A list of string values.",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="a string of value"
                    ))
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="The file to write content within, relative to the working directory.",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="String text which you write within a file.",
            ),
        },
    ),
)
