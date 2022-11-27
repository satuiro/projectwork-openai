# All the imports
import os
import openai

from dotenv import load_dotenv
load_dotenv()

# Load the secret API Key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def returnText(txt):
    # Gets response from the open-ai API server
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=txt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    ) #All the settings for the functionality

    # return the response back to app.py
    return response.choices[0].text