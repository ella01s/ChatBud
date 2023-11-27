# -*- coding: utf-8 -*-
"""ChatBud01.ipynb

Original file is located at
    https://colab.research.google.com/drive/1hyvr6BagYR6Cef9e8VAacNpnPejmXpZf
    
Author: Ella Solomon
Last update: 25/11/23
Description: Rule based chat bot - ChatBud
"""

import re
import sys
from nltk.chat.util import Chat, reflections

# Initialize context variables
user_name = None
conversation_history = []

pairs = [
    ['(.*) my name is (.*)', ['hi %2']],
    ['(hi|hello|hey|howexiedy|hi there|hey there|greetings|salutations|yo|hiya|hola)', ['hello', 'hi', 'hey', 'hey there', 'hi there', 'hiya']],
    ['(.*) in (.*) is (.*)', ['%1 in %2 is indeed %3']],
    ['(.*) created you?', ['Ella Solomon, using the nltk package']],
    ['(.*) help (.*)', ['contact linkedin.com/in/ella-solomon-a317621b0 for help']],
    ['exit|goodbye|bye', ['Goodbye!', 'See you later!', 'Goodbye, have a great day!']]

]

# Print the introductory phrase only once
print("Hello my name is ChatBud, but you can call me Bud for short.")

"""
# Check if the user's name has been provided.
if user_name:
    # If the name is known, prompt the user with their name.
    user_input = input(f"{user_name}: ")
else:
    # If the name is not known, use "Me" as the default name.
    user_input = input("Me: ")
    """

chat = Chat(pairs, reflections)

while True:
    # Get the next user input
    user_input = input(f"{user_name or 'Me'}: ")
    
    # Append the user's input to the conversation history.
    conversation_history.append(user_input)

    # Generate a response from the chatbot based on the user's input.
    response = chat.respond(user_input)

    # Check if the user provided their name in the current input.
    if 'my name is' in user_input:
        # Extract and store the user's name from the input.
        user_name = re.search('my name is (.*)', user_input).group(1)

    # Check if the user wants to exit the conversation.
    if re.search(r'\b(exit|goodbye|bye)\b', user_input.lower()):
        # Generate a response for the "exit" command and exit the loop.
        response = chat.respond('exit')

        print("Bud:", response)
        # Reset username
        user_name = None
        # Clear the conversation history when exiting.
        conversation_history.clear()
        #exit loop
        break 
    
    #Generate repsonse 
    response = chat.respond(user_input)
    
    # Check if the user provided their name in the current input.
    if 'my name is' in user_input:
        # Extract and store the user's name from the input.
        user_name = re.search('my name is (.*)', user_input).group(1)

    # Print the chatbot's response
    print("Bud:", response)

    # Check if the user is asking for directions
    directions_pattern = re.compile(r'\b(directions?|navigate|how to get|get from|travel from)\b(.+?)\b(to|in)\b(.+)$', re.IGNORECASE)
    # Extract start and end destinations using patterns
    location_match = directions_pattern.search(user_input.lower())

    if location_match:
        start_location = location_match.group(2).strip()
        end_location = location_match.group(4).strip()

        # Response
        response = f"To get from {start_location} to {end_location}, follow these steps: "

        # Print the chatbot's response
        print("Bud:", response)

    # Get the next user input
    user_input = input(f"{user_name or 'Me'}: ")
