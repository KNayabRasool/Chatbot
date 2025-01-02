import openai
from chatbot.responses import predefined_responses
from chatbot.config import OPENAI_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_response(user_input):
    """
    Process user input and return the chatbot's response.
    """
    # Check if the input matches predefined intents
    for intent, response in predefined_responses.items():
        if intent in user_input.lower():
            return response

    # Use OpenAI Chat API for generative responses
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if needed
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
