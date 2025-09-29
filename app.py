import requests
import streamlit as st

def send_message(user_message):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": user_message}
        ).json()
        return response["response"]
    except requests.exceptions.RequestException as e:
        return f"Error connecting to backend: {e}"

user_input = st.text_input("Your message:")
if st.button("Send"):
    reply = send_message(user_input)
    st.write(reply)
