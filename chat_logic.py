# chat_logic.py
def get_response(user_input):
    greetings = ["hi", "hello", "hey","Harish"]
    if any(word in user_input.lower() for word in greetings):
        return "Hello! I'm your friendly AI chatbot. How can I help you today?"
    else:
        return f"Sorry, I didn't understand: '{user_input}'. Can you rephrase?"
