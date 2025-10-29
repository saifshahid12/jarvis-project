# main.py
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Create a chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Google Cloud and Alexa."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the assistant's reply
print(completion.choices[0].message.content)
