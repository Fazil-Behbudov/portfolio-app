import streamlit as st
import pandas as pd

# Set layout to wide screen
st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("images/fazil.png", width=440)

with col2:
    st.markdown("### 👨‍💻 Behbudov Fazil")
    st.info("""
    I'm a Computer Science student at **UFAZ (French-Azerbaijani University)**, with a strong interest in **data science**.

    My studies and projects involve analyzing data, identifying patterns, and drawing meaningful insights from information.  
    I'm continuously developing my skills through academic work and independent learning, with a focus on solving real-world problems using **data-driven approaches**.
    """)


st.markdown("### 🧪 Python Projects")
st.write("Below you can find some of the apps I have built in Python. Feel free to contact me.")



# Project cards layout
col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv('data.csv',sep=';')
with col3:
    for index,row in df[0:10].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image(f'images/{row['image']}')
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image(f'images/{row['image']}')
        st.write(f"[Source Code]({row['url']})")