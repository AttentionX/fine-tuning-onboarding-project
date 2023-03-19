import os
import openai

# Set the OpenAI API key from the .env file
# from dotenv import load_dotenv

# load_dotenv()

# Define the OpenAI API parametersx
# openai.api_key = '<YOUR_OPENAI_API_KEY>'
openai.api_key = os.environ.get('OPENAI_API_KEY')

def ft_gpt(chat_history):
    max_tokens = 500
    temperature = 0.1
    response = openai.Completion.create(
        model="",
        prompt=chat_history,
        temperature=temperature, 
        max_tokens=max_tokens
    )
    answer = response.choices[0]['text']
    return answer

def gpt3(chat_history):
    engine = "text-davinci-003"
    max_tokens = 500
    temperature = 0.1
    response = openai.Completion.create(
        engine=engine, 
        prompt=f'{chat_history}',
        temperature=temperature, 
        max_tokens=max_tokens
    )

    answer = response.choices[0]['text']
    return answer