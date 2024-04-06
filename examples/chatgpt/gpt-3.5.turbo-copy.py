import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
print('openapi key:::', openai.api_key)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Capital of U.S.A ?\n" }],#,
              #"content": "What is the Capital of U.S.A ?\n" }],op
    temperature=0,
    max_tokens=101,
    stop=["\n"]
)

response1 = response['choices'][0]['message']

#$ openai api completions.create -m text-davinci-003 -p "Say this is a test" -t 0 -M 7 --stream

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[  # {"role": "system",
#         # "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01"},
#         # {"role": "user", "content": "How are you?"},
#         # {"role": "assistant", "content": "I am doing well"},
#         {"role": "user", "content": "What is the current GPT model ?\n",
#          "role": "user", "content": "What is the Capital of U.S.A ?"}],
#     temperature=0,
#     max_tokens=51,
#     top_p=1,
#     frequency_penalty=0.0,
#     presence_penalty=0.0,
#     stop=["\n"]
# )
print('response is::', response1)
