import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Dictionary mapping each letter to its Google Drive direct download link
IMAGE_URLS = {

'a': 'https://drive.google.com/uc?export=download&id=11E6lCsp9AFQq2ElzfZQ_UrV9RihMuIEV',
'b': 'https://drive.google.com/uc?export=download&id=1Od5a7OYDvjCHB0xwle6muPoAvpPiUvnQ',
'c': 'https://drive.google.com/uc?export=download&id=1v9vumaz2j4zqlqPi9UmRtW1v2LnZ1xh5',
'd': 'https://drive.google.com/uc?export=download&id=10POxe4_I6yG1n-G_e_XOpWzyzU3w8Q9v',
'e': 'https://drive.google.com/uc?export=download&id=1LWPNSq8-nqQCfI8lrGlNy2URWYTL_f16',
'f': 'https://drive.google.com/uc?export=download&id=18uC07m2EzYDSnfry9dsOTP0t-sXZ3cH3',
'g': 'https://drive.google.com/uc?export=download&id=1XGGYwDkNbb4XvyLGcQXzyKK6Jxxc8fHK',
'h': 'https://drive.google.com/uc?export=download&id=1xim-dJ3hor2DYPXIqkZMXcyT6ONHRsvk',
'i': 'https://drive.google.com/uc?export=download&id=1gWseklvAmNGmqqZFjzvowVxxQd__ILQ5',
'j': 'https://drive.google.com/uc?export=download&id=1RgNwPFB1Tw7NMLYnPyKissZbgg0OyvVd',
'k': 'https://drive.google.com/uc?export=download&id=18ylfC5jfX8Sz_ayWbRgMM668WPZlIV8-',
'l': 'https://drive.google.com/uc?export=download&id=1NCLeWc7MAfrdlo-Gh3U0yCQSiHLslCz1',
'm': 'https://drive.google.com/uc?export=download&id=1K74XQACJvp-xWvv29Sp2EKEYz4vMTUfk',
'n': 'https://drive.google.com/uc?export=download&id=1y6_NPjnVpqRMZoWjGHcwNyWw0qMgD2kZ',
'o': 'https://drive.google.com/uc?export=download&id=17tT9PjtOdZz_qwun1e3GM3d68IfQpdSZ',
'p': 'https://drive.google.com/uc?export=download&id=12niQPGHKd4W7YbD68XqTioCJIHjuQlFJ',
'q': 'https://drive.google.com/uc?export=download&id=1Takk-V-Y7pZER8Kpa_aWLn7IxWFLiOui',
'r': 'https://drive.google.com/uc?export=download&id=1Oe_7DkaRHSO82kjTZv3zPwZPOjeLp3W3',
's': 'https://drive.google.com/uc?export=download&id=1U1IvQzhGhEg5mC85Y3SDexSsxtSeFAZ9',
't': 'https://drive.google.com/uc?export=download&id=13Uajzk6bA8K4abrd0JykMO-o1x6SA2lJ',
'u': 'https://drive.google.com/uc?export=download&id=1RRIE3wYBFJu_n4hSHvIrqcDq_uTbOxEg',
'v': 'https://drive.google.com/uc?export=download&id=1gDJxItXS_qUAK-lcC_pnkoSOr5KK6b8O',
'w': 'https://drive.google.com/uc?export=download&id=1vwdr1IYpZc-vJ_nxpYSDl2KuYJ7roLt-',
'x': 'https://drive.google.com/uc?export=download&id=1ll2rKEkQZRp_Jvv5YOind8gxDWmW65tD',
'y': 'https://drive.google.com/uc?export=download&id=1z4bDQzWSAg4bLSmfmfSgJfVQOjagqvgY',
'z': 'https://drive.google.com/uc?export=download&id=1pbcNSgMMJ8PsFFmmg5FdXmYMkNr113Yo'

}


def load_image_from_url(char):
    """Fetch image from Google Drive direct link."""
    url = IMAGE_URLS.get(char)
    if url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                return img
            else:
                st.write(f"Failed to fetch image for: {char}")
        except Exception as e:
            st.write(f"Error loading image for {char}: {e}")
    return None

def display_sign_language(text):
    """Display sign language images for input text in a single line."""
    # Create a list of columns, one for each character
    columns = st.columns(len(text))
    
    for i, char in enumerate(text.lower()):
        if char.isalpha():  # Display images only for alphabets
            img = load_image_from_url(char)
            if img:
                with columns[i]:
                    st.image(img, width=80, caption=char.upper(), use_container_width=False)

        elif char == ' ':
            with columns[i]:
                st.write(" ")  # Blank column for space

# Streamlit Interface
st.title("Vartalaap Setu")
st.subheader("Text to Sign Language Converter")
st.write("Enter text below, and see it translated into sign language alphabets!")

# Input text box
text_input = st.text_input("Enter text here:")

if st.button("Convert"):
    if text_input.strip():  # Check if input is not empty
        display_sign_language(text_input)
    else:
        st.write("Please enter some text.")