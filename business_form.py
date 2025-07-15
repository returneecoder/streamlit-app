import streamlit as st
from google import genai
from PIL import Image

def show_business_form():
    mybot = genai.Client(api_key="AIzaSyDMD6OqYaq04FoOu2dt_NUZuplfPi6oQN0")

    spacer1, btn1_col, btn2_col, btn3_col = st.columns([5, 1, 1, 1])

    with btn1_col:
        if st.button('Home'):
            st.write("you clicked home button")

    with btn2_col:
        if st.button('login'):
            st.write("you clicked login button")

    with btn3_col:
        if st.button('signin'):
            st.write("you clicked sign in button")

    col1, col2 = st.columns(2)
    with col1:
        st.title("Describe your business ideas here")
        business_name = st.text_input("Enter your business name")
        business_description = st.text_area("Enter your business description")
        target_audience = st.text_area("Enter your target audience")
        current_capital = st.text_area("Enter your current capital")
        location = st.text_input("Enter your location")

        if st.button('Generate'):
            if business_description and business_name and target_audience and current_capital:
                question = (
                    f"My business name: {business_name}. "
                    f"My business description: {business_description}. "
                    f"My target audience: {target_audience}. "
                    f"My current capital: {current_capital}. "
                    f"My location: {location}. "
                    "Can you provide suggestions to improve my business?"
                )
                response = mybot.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=question
                )
                st.subheader("AI Suggestion")
                if response.text:
                    st.write(response.text)
            else:
                st.error("Please fill out the required fields")

    with col2:
        img_path = "robo.jpg"
        try:
            mypick = Image.open(img_path)
            st.image(mypick.convert("RGB"))
        except FileNotFoundError:
            st.warning("Image not found: robo.jpg")
