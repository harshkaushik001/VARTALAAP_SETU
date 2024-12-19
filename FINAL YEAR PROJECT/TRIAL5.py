import streamlit as st
from PIL import Image
import os

def load_image(char):
    """Load image for the given character."""
    image_path = f"sign_images/{char}.png"
    if os.path.exists(image_path):
        return Image.open(image_path)
    return None

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
st.sidebar.title("Vartalaap Setu")
st.sidebar.markdown("**Navigation**")
menu_option = st.sidebar.radio("Go to", ("Home", "About", "More"))
st.sidebar.markdown("**Options**")
st.sidebar.selectbox("Change Language", ["English", "Hindi", "Spanish"])

if menu_option == "Home":
    st.title("Vartalaap Setu")
    st.subheader("Text to Sign Language Converter")
    st.write("Enter text below, and see it translated into sign language alphabets!")

    text_input = st.text_input("Enter text here:")

    if st.button("Convert"):
        if text_input.strip():
            display_sign_language(text_input)
        else:
            st.write("Please enter some text.")

elif menu_option == "About":
    st.title("About Vartalaap Setu")
    st.write("Vartalaap Setu is a tool designed to bridge communication gaps by converting text into sign language. This application helps promote inclusivity and ease of communication.")

elif menu_option == "More":
    st.title("More Information")
    st.write("Explore additional features and details about Vartalaap Setu. Future updates will include support for dynamic sign language gestures and more languages.")
