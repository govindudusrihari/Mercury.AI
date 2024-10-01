# Stage 9:  Handling Multiple User Sessions

import os
import sys
from dotenv import load_dotenv
import requests
import json
import threading # For concurrent processing of user sessions

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
    # ... (Code from Stage 8) ...

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

# Define function to handle individual user conversations
def handle_conversation(user_id, user_data):
    """
    Handles conversation flow for a single user in a separate thread. 
    """

    conversation_history = []
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break
        
        response = get_gemini_response(user_message, conversation_history, user_data)
        print(f"\nChatbot: {response}") 

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(f"\n{recommendations}")

        # Update conversation history
        conversation_history.append((user_message, response))

# Main loop: manages authentication and starts new threads for each user
if __name__ == "__main__":
    print("Welcome to the Student Support Chatbot!")
    while True:
        user_id = input("Enter your ID: ")
        user_data = {}  # Placeholder, load actual data as needed
        if authenticate_user(user_id, user_data):
            print("Authentication successful!")
            # Create a new thread to handle conversation for this user
            thread = threading.Thread(target=handle_conversation, args=(user_id, user_data))
            thread.start()  
        else:
            print("Access denied. Please provide valid authentication details.")
# Stage 10:  Improving Chatbot's Memory and Knowledge

import os
import sys
from dotenv import load_dotenv
import requests
import json
import threading

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 8) ...

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

# Define function to handle individual user conversations
def handle_conversation(user_id, user_data):
    """
    Handles conversation flow for a single user, with memory enhancements.
    """

    conversation_history = []
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break
        
        # Enhance memory: Add user_data to conversation history
        conversation_history.append((user_message, user_data)) 

        response = get_gemini_response(user_message, conversation_history, user_data)
        print(f"\nChatbot: {response}")

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(f"\n{recommendations}")

        # Update conversation history 
        conversation_history.append((user_message, response))

        # Example: Update user_data based on conversation
        if 'course' in user_message:
            user_data['course'] = user_message.split('course')[-1].strip() 
            save_user_profile(user_id, user_data)
            print(f"\nI've noted your course: {user_data['course']}") 

# Main loop: manages authentication and starts new threads for each user
if __name__ == "__main__":
    print("Welcome to the Student Support Chatbot!")
    while True:
        user_id = input("Enter your ID: ")
        user_data = load_user_profile(user_id)  # Load profile from file
        if authenticate_user(user_id, user_data):
            print("Authentication successful!")
            # Create a new thread to handle conversation for this user
            thread = threading.Thread(target=handle_conversation, args=(user_id, user_data))
            thread.start()  
        else:
            print("Access denied. Please provide valid authentication details.")
# Stage 11: Improving Error Handling and Fallback Mechanisms

import os
import sys
from dotenv import load_dotenv
import requests
import json
import threading

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 8) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None):
    """
    Sends a user message to the Gemini API with conversation history,
    user data (optional), and returns the response. Handles errors gracefully 
    and includes fallback mechanisms.
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
        return "I'm having trouble connecting right now. Please try again later."
    except KeyError as e:
        print(f"Error decoding response from Gemini: {e}")
        return "Oops! Something went wrong. Let's try that again."

# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    # ... (Code from Stage 5) ...

# Define function to load user profile data from file
def load_user_profile(user_id):
    # ... (Code from Stage 6) ...

# Define function to save user profile data to file
def save_user_profile(user_id, user_data):
    # ... (Code from Stage 6) ...

# Define function to handle individual user conversations
def handle_conversation(user_id, user_data):
    """
    Handles conversation flow for a single user, with enhanced error handling and 
    fallback mechanisms.
    """

    conversation_history = []
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break
        
        conversation_history.append((user_message, user_data)) 

        response = get_gemini_response(user_message, conversation_history, user_data)

        # Fallback mechanism: Provide generic response if Gemini fails 
        if 'Please try again later' in response or 'Oops!' in response:
            response = "I'm still learning. Could you rephrase your question?"

        print(f"\nChatbot: {response}")

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(f"\n{recommendations}")

        conversation_history.append((user_message, response))

        # ... (Code for updating user_data, as in Stage 10) ...

# Main loop: manages authentication and starts new threads for each user
if __name__ == "__main__":
    print("Welcome to the Student Support Chatbot!")
    while True:
        user_id = input("Enter your ID: ")
        user_data = load_user_profile(user_id)
        if authenticate_user(user_id, user_data):
            print("Authentication successful!")
            thread = threading.Thread(target=handle_conversation, args=(user_id, user_data))
            thread.start()  
        else:
            print("Access denied. Please provide valid authentication details.")
# Stage 12: Introducing Interactive Elements

import os
import sys
from dotenv import load_dotenv
import requests
import json
import threading
import random # For randomizing options

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 8) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None):
    # ... (Code from Stage 11 with enhanced error handling and fallback) ...

# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    # ... (Code from Stage 5) ...

# Define function to load user profile data from file
def load_user_profile(user_id):
    # ... (Code from Stage 6) ...

# Define function to save user profile data to file
def save_user_profile(user_id, user_data):
    # ... (Code from Stage 6) ...

# Define a simple quiz function (placeholder)
def run_quiz(user_data):
    """
    Presents a simple quiz with questions relevant to stress management or study skills.
    
    Args:
        user_data (dict): User data dictionary.

    Returns:
        str: Feedback on the quiz.
    """

    questions = [
        {"question": "What's the most effective way to handle exam anxiety?", 
         "options": ["Procrastinate", "Avoid studying", "Practice deep breathing", "Stay up all night"],
         "answer": 3}, 
        # ... Add more questions ...
    ]

    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{j+1}. {option}")
        choice = int(input("Enter your choice (1-4): "))
        if choice == question['answer']:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The answer was {question['answer']}.")

    feedback = ""
    if score >= len(questions) / 2:
        feedback += "You did great on the quiz!" 
    else:
        feedback += "Don't worry - practice makes perfect. Review the questions you got wrong!"
    
    return feedback

# Define function to handle individual user conversations
def handle_conversation(user_id, user_data):
    """
    Handles conversation flow for a single user, now with interactive elements. 
    """

    conversation_history = []
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break

        conversation_history.append((user_message, user_data)) 

        response = get_gemini_response(user_message, conversation_history, user_data)

        # Fallback mechanism: Provide generic response if Gemini fails 
        if 'Please try again later' in response or 'Oops!' in response:
            response = "I'm still learning. Could you rephrase your question?"

        print(f"\nChatbot: {response}")

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(f"\n{recommendations}")

        # Interactive Element - Trigger a quiz based on context
        if 'quiz' in user_message.lower():
            quiz_feedback = run_quiz(user_data)
            print(f"\n{quiz_feedback}") 

        conversation_history.append((user_message, response))

        # ... (Code for updating user_data, as in Stage 10) ...

# Main loop: manages authentication and starts new threads for each user
if __name__ == "__main__":
    print("Welcome to the Student Support Chatbot!")
    while True:
        user_id = input("Enter your ID: ")
        user_data = load_user_profile(user_id)
        if authenticate_user(user_id, user_data):
            print("Authentication successful!")
            thread = threading.Thread(target=handle_conversation, args=(user_id, user_data))
            thread.start()  
        else:
            print("Access denied. Please provide valid authentication details.")
# Stage 13: Integrating with External Resources

import os
import sys
from dotenv import load_dotenv
import requests
import json
import threading
import random

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 8) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None):
    # ... (Code from Stage 11 with enhanced error handling and fallback) ...

# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    # ... (Code from Stage 5) ...

# Define function to load user profile data from file
def load_user_profile(user_id):
    # ... (Code from Stage 6) ...

# Define function to save user profile data to file
def save_user_profile(user_id, user_data):
    # ... (Code from Stage 6) ...

# Define a simple quiz function (placeholder)
def run_quiz(user_data):
    # ... (Code from Stage 12) ...

# **Example:** Function to access a university calendar API 
# This is a placeholder - you will need to replace it with the actual API documentation for your university
def get_university_calendar_data(university_id):
    """
    Retrieves upcoming events from a university calendar API. 

    Args:
        university_id (str): The ID of the university. 

    Returns:
        list: A list of upcoming events, or an empty list if no events are found.
    """
    url = f"https://api.universitycalendar.com/{university_id}/events"
    headers = {
        "Authorization": "Your API Key" 
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        events = response.json()['events'] 
        return events
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to University Calendar API: {e}")
        return []
    except KeyError as e:
        print(f"Error decoding response from University Calendar API: {e}")
        return [] 

# Define function to handle individual user conversations
def handle_conversation(user_id, user_data):
    """
    Handles conversation flow for a single user, now with integrated external resources.
    """

    conversation_history = []
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break

        conversation_history.append((user_message, user_data)) 

        response = get_gemini_response(user_message, conversation_history, user_data)

        # Fallback mechanism: Provide generic response if Gemini fails 
        if 'Please try again later' in response or 'Oops!' in response:
            response = "I'm still learning. Could you rephrase your question?"

        print(f"\nChatbot: {response}")

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(f"\n{recommendations}")

        # Interactive Element - Trigger a quiz based on context
        if 'quiz' in user_message.lower():
            quiz_feedback = run_quiz(user_data)
            print(f"\n{quiz_feedback}") 

        # Integrate with external resource 
        if "calendar" in user_message.lower() or "events" in user_message.lower():
            university_id = "your_university_id" #  Replace with your university's ID 
            events = get_university_calendar_data(university_id)
            if events:
                print("\nUpcoming Events:")
                for event in events:
                    print(f"- {event['title']} ({event['date']})")
            else:
                print("No upcoming events found.") 

        conversation_history.append((user_message, response))

        # ... (Code for updating user_data, as in Stage 10) ...

# Main loop: manages authentication and starts new threads for each user
if __name__ == "__main__":
    print("Welcome to the Student Support Chatbot!")
    while True:
        user_id = input("Enter your ID: ")
        user_data = load_user_profile(user_id)
        if authenticate_user(user_id, user_data):
            print("Authentication successful!")
            thread = threading.Thread(target=handle_conversation, args=(user_id, user_data))
            thread.start()  
        else:
            print("Access denied. Please provide valid authentication details.")
# Stage 14: Improving Response Generation with Gemini Parameters

import os
import sys
from dotenv import load_dotenv
import requests
import json
import threading
import random

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Define function to check user authentication (from Stage 1)
def authenticate_user(user_id, user_data):
    # ... (Code from Stage 1) ...

# Define function to get user input
def get_user_input():
    # ... (Code from Stage 8) ...

# Define function to get a response from the Gemini API
def get_gemini_response(user_message, conversation_history=[], user_data=None, 
                        temperature=0.7, top_k=40, top_p=0.95, presence_penalty=0.0, frequency_penalty=0.0):
    """
    Sends a user message to the Gemini API with conversation history,
    user data (optional), and specified Gemini parameters. Handles errors gracefully 
    and includes fallback mechanisms.
    """

    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'message': user_message,
        'conversation_history': conversation_history,
        'temperature': temperature, 
        'top_k': top_k, 
        'top_p': top_p, 
        'presence_penalty': presence_penalty, 
        'frequency_penalty': frequency_penalty, 
        'user_data': user_data
    }
    try:
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['content']
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Gemini API: {e}")
        return "I'm having trouble connecting right now. Please try again later."
    except KeyError as e:
        print(f"Error decoding response from Gemini: {e}")
        return "Oops! Something went wrong. Let's try that again."

# Define a function to get personalized recommendations based on Gemini's response
def get_recommendations(response, user_data):
    # ... (Code from Stage 5) ...

# Define function to load user profile data from file
def load_user_profile(user_id):
    # ... (Code from Stage 6) ...

# Define function to save user profile data to file
def save_user_profile(user_id, user_data):
    # ... (Code from Stage 6) ...

# Define a simple quiz function (placeholder)
def run_quiz(user_data):
    # ... (Code from Stage 12) ...

# **Example:** Function to access a university calendar API 
# This is a placeholder - you will need to replace it with the actual API documentation for your university
def get_university_calendar_data(university_id):
    # ... (Code from Stage 13) ... 

# Define function to handle individual user conversations
def handle_conversation(user_id, user_data):
    """
    Handles conversation flow for a single user, now with integrated external resources.
    """

    conversation_history = []
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'quit':
            break

        conversation_history.append((user_message, user_data)) 

        # Use parameters to modify response style
        # This is a simplified example - you can modify these parameters as needed
        response = get_gemini_response(user_message, conversation_history, user_data,
                                    temperature=0.5, top_k=50) # More focused output with some creativity

        # Fallback mechanism: Provide generic response if Gemini fails 
        if 'Please try again later' in response or 'Oops!' in response:
            response = "I'm still learning. Could you rephrase your question?"

        print(f"\nChatbot: {response}")

        recommendations = get_recommendations(response, user_data)
        if recommendations:
            print(f"\n{recommendations}")

        # Interactive Element - Trigger a quiz based on context
        if 'quiz' in user_message.lower():
            quiz_feedback = run_quiz(user_data)
            print(f"\n{quiz_feedback}") 

        # Integrate with external resource 
        if "calendar" in user_message.lower() or "events" in user_message.lower():
            university_id = "your_university_id" 
            events = get_university_calendar_data(university_id)
            if events:
                print("\nUpcoming Events:")
                for event in events:
                    print(f"- {event['title']} ({event['date']})")
            else:
                print("No upcoming events found.") 

        conversation_history.append((user_message, response))

        # ... (Code for updating user_data, as in Stage 10) ...

# Main loop: manages authentication and starts new threads for each user
if __name__ == "__main__":
    print("Welcome to the Student Support Chatbot!")
    while True:
        user_id = input("Enter your ID: ")
        user_data = load_user_profile(user_id)
        if authenticate_user(user_id, user_data):
            print("Authentication successful!")
            thread = threading.Thread(target=handle_conversation, args=(user_id, user_data))
            thread.start()  
        else:
            print("Access denied. Please provide valid authentication details.")
# Stage 15: Improving User Authentication and Security

import os
import sys
from dotenv import load_dotenv
import requests
import json
import threading
import random
from cryptography.fernet import Fernet # Placeholder encryption example

# Load environment variables from a .env file (optional for API keys, etc.)
load_dotenv()

# Define global variables for configuration
API_KEY = os.getenv('API_KEY')
USER_AUTH_MODE = 'email'
GEMINI_API_ENDPOINT = "https://api.gemini.google.com/v1/chat"

# Generate a key for encryption (replace this with secure key management)
key = Fernet.generate_key() 
cipher_suite = Fernet(key)

# ... (Code from previous stages - get_user_input, etc.) ...

# Example enhanced authentication function 
#  - Uses a placeholder 2FA method and encryption
def authenticate_user(user_id, user_data):
    # ... (code for email-based authentication - replace with real implementation)

    if user_id and "@" in user_id: # Assuming email based authentication
        # 2FA (replace with real 2FA implementation) 
        two_factor_code = input("Enter your two-factor code: ") 
        if verify_2fa_code(user_id, two_factor_code):  # Check the 2FA code (replace with real logic)
            return True
    
    print('Authentication failed') 
    return False 

# Example placeholder function for encrypting user data
def encrypt_user_data(user_data):
    """
    Encrypts the user data using Fernet. 

    Args:
        user_data (dict): The user data to encrypt. 

    Returns:
        dict: Encrypted user data. 
    """
    encrypted_data = {}
    for key, value in user_data.items():
        encrypted_data[key] = cipher_suite.encrypt(value.encode()).decode()
    return encrypted_data

# Example placeholder function for decrypting user data 
def decrypt_user_data(encrypted_data):
    """
    Decrypts user data using Fernet. 

    Args:
        encrypted_data (dict): The encrypted user data to decrypt.

    Returns:
        dict: Decrypted user data. 
    """
    decrypted_data = {}
    for key, value in encrypted_data.items():
        decrypted_data[key] = cipher_suite.decrypt(value.encode()).decode()
    return decrypted_data 


# Example loading and saving user profile 
# (You will need to adjust this for the chosen database implementation)
def load_user_profile(user_id):
    # ... (code for loading profile from database, remember to decrypt the data if necessary)

def save_user_profile(user_id, user_data):
    # ... (code for saving the profile to database, remember to encrypt the data before saving)

# ... (rest of the code -  get_gemini_response, run_quiz, get_university_calendar_data, handle_conversation) ...
