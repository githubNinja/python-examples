import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



prompt = f"""
Generate a list of 5 famous Chicago basket players with their names, date of birth along with their team name \ 
with their team id, player name and date of birth. 
Provide them in JSON format with the following keys: 
player_name, date_of_birth, team_name
"""

response = get_completion(prompt)

print(response)
