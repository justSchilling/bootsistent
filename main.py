import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

# technically needs additional validation since we add a 3rd param
if len(sys.argv) < 2 or not sys.argv[1]:
    print(
        "This call is bad. Like, very bad. We can't go on like this. please provide a "
        + "single string prompt as argument for this script",
    )
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
unused = 15

prompt = sys.argv[1]
messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

print(response.text)
if "--verbose" in sys.argv and response.usage_metadata:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
