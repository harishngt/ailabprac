# Define a dictionary with some predefined responses
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am SimpleBot. What's your name?",
    "bye": "Goodbye! Have a nice day!",
    "exit": "Goodbye! Have a nice day!",
    "quit": "Goodbye! Have a nice day!",
}

def get_response(user_input):
    # Normalize the user input to lower case
    normalized_input = user_input.lower()
    # Find the response in the dictionary or return a default message
    return responses.get(normalized_input, "I'm sorry, I don't understand that.")

def chat():
    print("Type something to begin (type 'bye', 'exit', or 'quit' to end the chat)...")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("SimpleBot: Goodbye! Have a nice day!")
            break
        response = get_response(user_input)
        print(f"SimpleBot: {response}")

# Start the chat
if __name__ == "__main__":
    chat()
