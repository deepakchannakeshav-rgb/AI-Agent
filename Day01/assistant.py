from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from the .env file
load_dotenv()

# Create a client that communicates with Ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
print("*" * 40)
print("Welcome to the AI Agent! Type 'exit' to quit.")
print("*" * 40)
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting the AI Agent. Goodbye!")
        break

    # Send the user's input to the AI model
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    # Display the AI's response
    print("AI:", response.choices[0].message.content)   