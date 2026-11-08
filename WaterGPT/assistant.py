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
#create a list to store conversation
msges=[]
while True:
    user_input = input("You: ")

    #append the user input to the conversation list
    msges.append({"role":"user","content":user_input})
    if user_input.lower() == "exit":
        print("Exiting the AI Agent. Goodbye!")
        break

    # Send the user's input to the AI model
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=msges
    )

    # Display the AI's response
    print("AI:", response.choices[0].message.content)   

    #store the AI response in the conversation list
    msges.append({"role":"assistant","content":response.choices[0].message.content})

    #print conversation history
    for msg in msges:
        role = msg["role"]
        content = msg["content"]
        print(f"{role.capitalize()}: {content}")    