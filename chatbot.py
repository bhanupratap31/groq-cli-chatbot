import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = []

def chat_with_groq(user_input):
    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=conversation_history,
    )

    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return assistant_message

def main(): 
    print("Welcome to the Groq Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_groq(user_input)
        print(f"Groq: {response}")

if __name__ == "__main__":
    main()