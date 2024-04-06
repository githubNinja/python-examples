import os
import openai
OPENAI_API_KEY='#################'

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
print('openapi key:::', openai.api_key)

#Instructions - Set the API Key in venv terminal as

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Capital of India ?\n" }],
    temperature=0,
    max_tokens=101,
    stop=["\n"]
)

response1 = response['choices'][0]['message']

print('response is::', response1)
