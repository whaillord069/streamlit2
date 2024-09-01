import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center;'>My Autobiography</h1>", unsafe_allow_html=True)

st.image("me.jpg", caption="A Gentleman", use_column_width=True)

st.write("""
Greetings! I am John Gabriel Tejam, a student in Cebu Institute of Technology taking up
Information Technology. I enjoy playing chess, video games and watching anime. This simple
autobiography talks about little things about me.
""")

if 'display_section' not in st.session_state:
    st.session_state.display_section = None

col1, col2, col3, col4, col5 = st.columns([1, 0.1, 1, 0.1, 1])

with col1:
    if st.button('About Me'):
        st.session_state.display_section = 'about_me'


with col2:
    st.write("")

with col3:
    if st.button('Future Goals'):
        st.session_state.display_section = 'future_goals'

with col4:
    st.write("")

with col5:
    if st.button('Current Goal'):
        st.session_state.display_section = 'current_goal'

if st.session_state.display_section == 'about_me':
    st.header("ME!")
    st.write("**Full Name:** John Gabriel Rebosura Tejam")
    st.write("**Date of Birth:** June 30, 2000")
    st.write("**Age:** 24")
    st.write("**Place of Birth:** Cebu City")
    st.write("**Hobbies:** Playing chess, watching anime, playing video games, playing piano")
    st.write("**Favorite Quote:** Learning never exhausts the mind - Leonardo da Vinci")
    st.write("**Favorite music genre:** House music")

if st.session_state.display_section == 'future_goals':
    st.header("Future Goals")
    st.write("""
    Leave the country and work abroad!
    """)
    st.image("plane.jpg", use_column_width=True)
    st.write("""
    Live a comfortable life!        
    """)
    st.image("comfortable.jpg", use_column_width=True)


if st.session_state.display_section == 'current_goal':
    st.header("Current Goal")
    st.write("""
    Graduate this course and get a job.
    """)
    st.image("graduate.jpg", use_column_width=True)
    st.image("working2.jpg", use_column_width=True)

