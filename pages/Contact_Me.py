import streamlit as st
from send_mail import send_mail
st.set_page_config(layout='wide')
st.header("📬 Contact Me")
with st.form(key="contact_form"):
    st.write("I'd love to hear from you! Please fill out the form below.")
    user_email = st.text_input("Enter your email address")
    message = st.text_area("Enter your message")
    user_message = f"""\
Subject: New mail from {user_email}
\n
From: {user_email}
{message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_mail(user_message)
        st.success("Your message has been sent successfully!")