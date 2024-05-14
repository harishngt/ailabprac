import nltk
from nltk.chat.util import Chat, reflections
# Define patterns for the chatbot to recognize
patterns = [
(r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
(r'how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking.']),
(r'what is your name?', ['You can call me Chatbot.', 'I\'m Chatbot, nice to meet you.']),
(r'quit', ['Bye! Take care.']),
]
# Create a chatbot instance
chatbot = Chat(patterns, reflections)
# Start the conversation
print("Welcome to the Chatbot!")
print("Type 'quit' to exit.")
while True:
user_input = input("You: ")
response = chatbot.respond(user_input)
print("Chatbot:", response)
if user_input.lower() == 'quit':
break
