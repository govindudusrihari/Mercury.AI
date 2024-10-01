# Stage 1: Project Setup and Initial Dependencies

import os
import sys
from dotenv import load_dotenv

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv() 

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method

# Define function to check user authentication
def authenticate_user(user_id, user_data):
    """
    Verifies if a user is eligible for service.

    Args:
        user_id (str): User's ID.
        user_data (dict): User's data from authentication source (email, ID, etc.).

    Returns:
        bool: True if authenticated, False otherwise.
    """

    # This is a placeholder function for authentication logic.
    # You will need to replace it with your actual authentication implementation.
    # For example, you could validate student IDs or check emails against a database. 
    if USER_AUTH_MODE == 'email' and '@' in user_id:
        return True
    else:
        print('Invalid Authentication')
        return False

# Example usage
user_id = 'test@example.com'  # Input from user
user_data = {'student_id': '123456'}  # Sample data
is_authenticated = authenticate_user(user_id, user_data)
print(is_authenticated)

# Placeholder for Gemini API integration - to be added in later stages.
# You will need to include code to interact with Gemini using its APIs 
# based on your chosen framework. 
# Stage 2: User Input and Basic Conversation Flow

import os
import sys
from dotenv import load_dotenv

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv() 

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    """
    Gets user input from the console.
    
    Returns:
        str: User's input.
    """

    user_input = input("Enter your message: ")
    return user_input

# Define function to handle conversation flow
def handle_conversation():
    """
    Manages the basic conversation flow with the user.
    """

    print("Welcome to the Student Support Chatbot!")
    print("Please provide your authentication information (e.g., email, ID card):")
    user_id = input("Enter your ID: ")
    user_data = {} # Placeholder for additional user data
    if authenticate_user(user_id, user_data):
        print("Authentication successful!")
        while True:
            user_message = get_user_input()
            if user_message.lower() == 'quit':
                break
            # Here you would replace this placeholder with actual response generation using Gemini in the next stages. 
            response = "I am still under development. You said: " + user_message
            print(response)
    else:
        print("Access denied. Please provide valid authentication details.")


# Run the main conversation loop
handle_conversation()
# Stage 3: Basic Gemini Integration and Response Generation

import os
import sys
from dotenv import load_dotenv
import requests  # For making HTTP requests

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv() 

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat" 

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 2) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message):
    """
    Sends a user message to the Gemini API and returns the response.
    
    Args:
        user_message (str): The user's message.
    
    Returns:
        str: The response from the Gemini API.
    """

    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'message': user_message,
        'temperature': 0.7  # Adjust temperature for different response styles 
    }
    try:
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for any API errors
        return response.json()['content']  # Extract the content from the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Gemini API: {e}")
        return "I'm sorry, I couldn't understand your request. Please try again later."


# Define function to handle conversation flow
def handle_conversation():
    # ... (Code from Stage 2, including authentication) ...

    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break
        
        response = get_gemini_response(user_message)
        print(response)

# Run the main conversation loop
handle_conversation()
# Stage 4:  Contextual Understanding and Enhanced Responses

import os
import sys
from dotenv import load_dotenv
import requests  # For making HTTP requests

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv() 

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat" 

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 2) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[]):
    """
    Sends a user message to the Gemini API with conversation history 
    and returns the response.
    
    Args:
        user_message (str): The user's message.
        conversation_history (list): A list of tuples, where each tuple 
            contains (user_message, chatbot_response) from the previous 
            conversation turns.
    
    Returns:
        str: The response from the Gemini API.
    """

    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'message': user_message,
        'conversation_history': conversation_history, 
        'temperature': 0.7
    }
    try:
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['content']
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Gemini API: {e}")
        return "I'm sorry, I couldn't understand your request. Please try again later."

# Define function to handle conversation flow
def handle_conversation():
    # ... (Code from Stage 2, including authentication) ...

    conversation_history = []
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break
        
        response = get_gemini_response(user_message, conversation_history)
        print(response)

        # Update conversation history
        conversation_history.append((user_message, response))

# Run the main conversation loop
handle_conversation()
# Stage 5:  Personalized Recommendations and Resource Integration

import os
import sys
from dotenv import load_dotenv
import requests
import json

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 2) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None):
    """
    Sends a user message to the Gemini API with conversation history,
    user data (optional), and returns the response.

    Args:
        user_message (str): The user's message.
        conversation_history (list): A list of tuples, where each tuple
            contains (user_message, chatbot_response) from the previous
            conversation turns.
        user_data (dict, optional): Dictionary containing additional user information. Defaults to None.

    Returns:
        str: The response from the Gemini API.
    """

    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'message': user_message,
        'conversation_history': conversation_history,
        'temperature': 0.7,
        'user_data': user_data  # Pass user_data if available
    }
    try:
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['content']
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Gemini API: {e}")
        return "I'm sorry, I couldn't understand your request. Please try again later."


# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    """
    Analyzes the Gemini response and provides personalized recommendations.

    Args:
        response (str): The Gemini API response.
        user_data (dict): User data dictionary.

    Returns:
        str: Personalized recommendations string.
    """

    # Extract relevant keywords from the response using NLP techniques
    keywords = ["stress", "anxiety", "sleep", "motivation", "time management", "study tips", "finals"] 
    # Example: Consider keywords that might indicate a user's specific need
    found_keywords = [keyword for keyword in keywords if keyword in response.lower()]
    
    recommendations = ""
    if "stress" in found_keywords or "anxiety" in found_keywords:
        recommendations += "\nHere are some stress management resources: \n- https://www.mind.org.uk/information-support/types-of-mental-health-problems/anxiety-and-panic-attacks-\n- https://www.nhs.uk/conditions/stress-anxiety-depression/ "
    elif "sleep" in found_keywords:
        recommendations += "\nConsider trying these sleep-improving techniques: \n- https://www.nhs.uk/live-well/sleep-and-tiredness/how-to-get-a-good-nights-sleep/\n- https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/sleep/art-20047966 "
    else: 
        recommendations += "\nYou mentioned {0} - here are some relevant resources:".format(" ".join(found_keywords))

    return recommendations

# Define function to handle conversation flow
def handle_conversation():
    # ... (Code from Stage 2, including authentication) ...

    conversation_history = []
    user_data = {'student_id': '123456'}  # Placeholder for additional user data, replace with real information
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break
        
        response = get_gemini_response(user_message, conversation_history, user_data)
        print(response)

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(recommendations)

        # Update conversation history
        conversation_history.append((user_message, response))

# Run the main conversation loop
handle_conversation()
# Stage 6: User Profile Management and Persistence

import os
import sys
from dotenv import load_dotenv
import requests
import json

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 2) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None):
    # ... (Code from Stage 5) ...

# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    # ... (Code from Stage 5) ...

# Define function to load user profile data from file
def load_user_profile(user_id):
    """
    Loads user profile data from a JSON file.

    Args:
        user_id (str): User's ID.

    Returns:
        dict: User data dictionary if the file exists, otherwise an empty dictionary.
    """

    filename = f"{user_id}.json"  # File naming convention
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return {}

# Define function to save user profile data to file
def save_user_profile(user_id, user_data):
    """
    Saves user profile data to a JSON file.

    Args:
        user_id (str): User's ID.
        user_data (dict): User data dictionary.
    """

    filename = f"{user_id}.json"  # File naming convention
    with open(filename, 'w') as f:
        json.dump(user_data, f)

# Define function to handle conversation flow
def handle_conversation():
    # ... (Code from Stage 5, including authentication) ...

    conversation_history = []
    user_data = load_user_profile(user_id)
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break

        response = get_gemini_response(user_message, conversation_history, user_data)
        print(response)

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(recommendations)

        # Example of updating user profile data
        # You would replace this with actual interaction for collecting and storing information
        if 'new information' in response: 
            user_data['new_field'] = 'new_value'  # Update user profile
            save_user_profile(user_id, user_data)

        # Update conversation history
        conversation_history.append((user_message, response))

# Run the main conversation loop
handle_conversation()
# Stage 7: Error Handling and Robustness

import os
import sys
from dotenv import load_dotenv
import requests
import json

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 2) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None):
    """
    Sends a user message to the Gemini API with conversation history,
    user data (optional), and returns the response. Handles errors gracefully.

    Args:
        user_message (str): The user's message.
        conversation_history (list): A list of tuples, where each tuple
            contains (user_message, chatbot_response) from the previous
            conversation turns.
        user_data (dict, optional): Dictionary containing additional user information. Defaults to None.

    Returns:
        str: The response from the Gemini API or an error message.
    """

    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'message': user_message,
        'conversation_history': conversation_history,
        'temperature': 0.7,
        'user_data': user_data
    }
    try:
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['content']
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Gemini API: {e}")
        return "I'm sorry, I'm experiencing some technical difficulties. Please try again later."
    except KeyError as e:
        print(f"Error decoding response from Gemini: {e}")
        return "Oops! Something went wrong. I'm trying my best to get back on track. "

# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    # ... (Code from Stage 5) ...

# Define function to load user profile data from file
def load_user_profile(user_id):
    # ... (Code from Stage 6) ...

# Define function to save user profile data to file
def save_user_profile(user_id, user_data):
    # ... (Code from Stage 6) ...

# Define function to handle conversation flow
def handle_conversation():
    # ... (Code from Stage 6, including authentication) ...

    conversation_history = []
    user_data = load_user_profile(user_id)
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break
        
        response = get_gemini_response(user_message, conversation_history, user_data)
        print(response)

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(recommendations)

        # Update conversation history
        conversation_history.append((user_message, response))

# Run the main conversation loop
handle_conversation()
# Stage 8:  Improving User Interface and Interactivity

import os
import sys
from dotenv import load_dotenv
import requests
import json

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
#  - API_KEY can be retrieved from the .env file
#  - USER_AUTH_MODE defines authentication method (email, ID card, etc.)
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'  # Update this based on authentication method
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    """
    Gets user input from the console, adding some visual flair. 
    """

    user_input = input("You: ")
    return user_input

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None):
    # ... (Code from Stage 7 with error handling) ...

# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    # ... (Code from Stage 5) ...

# Define function to load user profile data from file
def load_user_profile(user_id):
    # ... (Code from Stage 6) ...

# Define function to save user profile data to file
def save_user_profile(user_id, user_data):
    # ... (Code from Stage 6) ...

# Define function to handle conversation flow
def handle_conversation():
    # ... (Code from Stage 7, including authentication) ...

    conversation_history = []
    user_data = load_user_profile(user_id)
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break

        response = get_gemini_response(user_message, conversation_history, user_data)
        print(f"\nChatbot: {response}") #  Improved output formatting

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(f"\n{recommendations}")

        # Update conversation history
        conversation_history.append((user_message, response))

# Run the main conversation loop
handle_conversation()
