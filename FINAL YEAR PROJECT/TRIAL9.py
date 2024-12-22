import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Custom CSS for styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fwhite%2520background%2F&psig=AOvVaw0FuD73dEmkfZPPYa4HGDbH&ust=1734676359243000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMjU9ZWbs4oDFQAAAAAdAAAAABAE");
    background-size: cover;
}
.stImage {
    background-color: white !important;  /* Add white background to images */
    border-radius: 8px;  /* Rounded corners */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);  /* Soft shadow */
}
.contact-us {
  color: white;
  text-align: left;
  font-size: 12px;  
  line-height: 1.4;  
  margin-top: 50px;
}
.faq {
  color: white;
  text-align: left;
  font-size: 12px;  
  line-height: 1.4;  
  margin-top: 50px;
}
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}
.divider {
  border-top: 2px solid white;
  margin: 20px 0;
}

/* To introduce space between the Convert button and FAQ/Contact Us sections */
.space {
    height: 150px; 
}

.stMarkdown, .stText {
    color: white;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Dictionary mapping each letter to its Google Drive direct download link
IMAGE_URLS = {
    'a': 'https://drive.google.com/uc?export=download&id=11E6lCsp9AFQq2ElzfZQ_UrV9RihMuIEV',
    'b': 'https://drive.google.com/uc?export=download&id=1Od5a7OYDvjCHB0xwle6muPoAvpPiUvnQ',
    'c': 'https://drive.google.com/uc?export=download&id=1v9vumaz2j4zqlqPi9UmRtW1v2LnZ1xh5',
    'd': 'https://drive.google.com/uc?export=download&id=1OzCqVdjDmWbp8x2Kngvzw1eKuWq83XOg',
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
    columns = st.columns(len(text))
    for i, char in enumerate(text.lower()):
        if char.isalpha():
            img = load_image_from_url(char)
            if img:
                with columns[i]:
                    # Display the sign image
                    st.image(img, caption=char.upper(), use_container_width=True)
                    # Display the alphabet corresponding to the sign
                    st.write(f"Letter: {char.upper()}")
        elif char == ' ':
            with columns[i]:
                st.empty()

# Streamlit Interface
def main():
    # Sidebar for navigation
    st.sidebar.title("Vartalaap Setu")
    st.sidebar.markdown("**Navigation**")
    menu_option = st.sidebar.radio("Go to", ("Home", "About", "More"))

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

        # Space before FAQ and Contact Us sections
        st.markdown('<div class="space"></div>', unsafe_allow_html=True)

        # Divider above FAQ and Contact Us sections
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)

        # Layout for FAQ and Contact Us sections
        col1, col2 = st.columns([2, 2])
        
        with col1:
            # FAQ section
            st.markdown("<h3>Frequently Asked Questions</h3>", unsafe_allow_html=True)
            st.markdown("""
                <p><strong>Q: What is Vartalaap Setu?</strong><br>A: Vartalaap Setu is a tool to convert text into sign language and promote inclusivity.</p>
                <p><strong>Q: How do I use it?</strong><br>A: Enter text in the input field, and it will display the corresponding sign language images.</p>
            """, unsafe_allow_html=True)

        with col2:
            # Contact Us section
            st.markdown("<h3>Contact Us</h3>", unsafe_allow_html=True)
            st.markdown("""
                <p>If you have any questions or suggestions, feel free to reach out to us:</p>
                <p>Email: support@vartalaapsetu.com</p>
                <p>Phone: +123 456 7890</p>
            """, unsafe_allow_html=True)

    elif menu_option == "About":
        st.title("About Vartalaap Setu")
        st.write("""
            Vartalaap Setu is an innovative web application designed to bridge the communication gap between individuals who use sign language and those who rely on text-based communication. 
            The tool aims to promote inclusivity, accessibility, and ease of interaction for people with hearing or speech disabilities.
        """)
        st.write("""
            **Purpose and Mission**
            Our mission is to provide a platform that enables seamless communication through sign language. 
            By converting text into sign language alphabets using visual representations, Vartalaap Setu empowers users to communicate more effectively and inclusively.
        """)
        st.write("""
            **Features**
            - **Text to Sign Language**: Convert any text input into sign language images representing alphabets.
            - **User-Friendly Interface**: Simple and intuitive design that allows anyone to easily interact with the tool.
            - **Custom Styling**: Visually appealing design with custom CSS to enhance user experience.
            - **Accessibility**: Aims to support individuals with hearing impairments by offering visual-based communication.
        """)

        st.write("""
            **Future Goals**
            We are continuously working to enhance the capabilities of Vartalaap Setu:
            - Real-time Sign Language to Text Conversion
            - Expanded Language Support
            - AI Integration
        """)

    elif menu_option == "More":
        st.title("More about Vartalaap Setu")
        st.write("""
            **More Information**
            **Upcoming Features**:
            - **Sign Language to Text**: Use your camera to interpret sign language gestures and convert them into text in real-time.
            - **Model Training**: Train a custom AI model to recognize different sign language gestures for better accuracy.
            - **Expanded Language Support**: Support for multiple sign languages (e.g., ASL, ISL) and multilingual text input.
            - **SignSync Challenge**: Test your knowledge and enhance your learning with the SignSync Challenge! Match the correct words with their corresponding signs and master the art of sign language in an interactive and fun way. Coming soon to Vartalaap Setu!
        """)

if __name__ == "__main__":
    main()
