import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


try:
    question = sys.argv[1]
except IndexError:
    raise sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=question)]),
]

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
print(response.text)

#TypeError: 'GenerateContentResponseUsageMetadata' object is not subscriptable
x = response.usage_metadata.prompt_token_count
y = response.usage_metadata.candidates_token_count

if  "--verbose" in sys.argv:
    print(f"User prompt: {question}")
    print(f"Prompt tokens: {x}")
    print(f"Response tokens: {y}")
    