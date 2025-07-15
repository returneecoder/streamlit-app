import streamlit as st
from google import  genai
from PIL import Image
from google.genai import types
from io import BytesIO


def show_image():
    myrobo = genai.Client(api_key="AIzaSyDMD6OqYaq04FoOu2dt_NUZuplfPi6oQN0")
    spacer1, btn1_col, btn2_col, btn3_col = st.columns([5, 1, 1, 1])

    with btn1_col:
        if st.button('Home'):
            st.write('Button 1 is clicked')
    with btn2_col:
        if st.button('Login'):
            st.write('login button  is clicked')
    with btn3_col:
        if st.button('Sign up'):
            st.write('signup button is clicked')

    col1, col2 = st.columns(2)
    with col1:
        st.title('Describe your Image here')
        content = st.text_area('')
        if st.button('visualize'):
            response = myrobo.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=content,
                config = types.GenerateContentConfig(
                    response_modalities=['TEXT','IMAGE'],
                )
            )
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    print(part.text)
                elif part.inline_data is not None:
                    image_bytes = part.inline_data.data  # This gives you raw bytes
                    image = Image.open(BytesIO(image_bytes))
                    image.save('MyImage.png')

    with col2:
        if st.image('MyImage.png'):
            st.write('your Image...')
        else:
            st.write('waiting for image...')
