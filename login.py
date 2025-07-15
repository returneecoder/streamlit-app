import streamlit as st
#from business_form import show_business_form
from ImageGenerate import show_image

USER_CREDENTIALS = {
    "admin": "1234",
    "user1": "abcd"
}

def login():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

def protected_area():
    st.title(f"👋 Welcome {st.session_state['username']}")
    show_image()

    #show_business_form()
    # ✅ Only show this after login

    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()

# App entry
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    login()
else:
    protected_area()
