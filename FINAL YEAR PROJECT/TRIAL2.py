import streamlit as st
from PIL import Image
import requests

def load_image(char):
    """Load image for the given character."""
    url = f"https://your-online-storage.com/{char}.png"
    return Image.open(requests.get(url, stream=True).raw)

def display_sign_language(text):
    """Display sign language images for input text."""
    for char in text.lower():
        if char.isalpha():
            img = load_image(char)
            if img:
                st.image(img, width=50, caption=char, use_column_width=False)
            else:
                st.write(f"Image not found for: {char}")
        elif char == ' ':
            st.write(" ")

# Streamlit Interface
st.title("Vartalaap Setu")
st.subheader("Text to Sign Language Converter")
st.write("Enter text below, and see it translated into sign language alphabets!")

text_input = st.text_input("Enter text here:")

if st.button("Convert"):
    if text_input.strip():
        display_sign_language(text_input)
    else:
        st.write("Please enter some text.")
