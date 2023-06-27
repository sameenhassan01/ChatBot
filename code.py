import numpy as np

# Load the data from file
filename = 'dialogs.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)
bot_responses = dict(data)

# Function to handle user input and provide responses
def chatbot():
    while True:
        user_input = input("User: ")
        matching_key = None
        for key in bot_responses:
            if key.lower() in user_input.lower():
                matching_key = key
                break

        if matching_key is not None:
            response = bot_responses[matching_key]
            print("ChatBot:", response)
            if response.lower() == "exit":
                break
        else:
            print("ChatBot: Sorry, I don't understand. Can you please ask a different question?")

# Start the chatbot
print("ChatBot: Hi, how can I help you today?")
chatbot()
