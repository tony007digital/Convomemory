# agents/openai_agent.py

import openai
import langchain as lc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OpenAIAgent(lc.Agent):
    def process(self, message):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.text,
            max_tokens=150,
            api_key=os.getenv('OPENAI_API_KEY')
        )
        return lc.Message(text=response['choices'][0]['text'].strip())
