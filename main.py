import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info , schema_write_file, schema_run_python_file, schema_get_file_content

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

try:
    question = sys.argv[1]
except IndexError:
    raise sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=question)]),
]

response = client.models.generate_content(model="gemini-2.0-flash-001",
                                          contents=messages,
                                          config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
),
                                          )

print(response.function_calls)
print(response.text)

#TypeError: 'GenerateContentResponseUsageMetadata' object is not subscriptable
x = response.usage_metadata.prompt_token_count
y = response.usage_metadata.candidates_token_count

if  "--verbose" in sys.argv:
    print(f"User prompt: {question}")
    print(f"Prompt tokens: {x}")
    print(f"Response tokens: {y}")
    