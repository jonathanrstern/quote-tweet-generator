import requests
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY_STERN")

text_davinci_002 = "https://api.openai.com/v1/engines/text-davinci-002/completions"
text_davinci_003 = "https://api.openai.com/v1/engines/text-davinci-003/completions"


def get_content_from_gpt(content):
    counter = 0
    error = True
    while error == True and counter < 5:
        try:
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"{content}"}]
            )
            gpt_choices = gpt_response.choices
            if len(gpt_choices):
                message = gpt_response.choices[0].message.content
                error = False
                return message
            raise Exception("No GPT Choices Present")
        except Exception as e:
            print('error getting gpt content:', e)
    print('tried and failed 5 times')
    return ""


