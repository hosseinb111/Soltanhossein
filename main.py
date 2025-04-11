import streamlit as st from supabase import create_client, Client import os

Supabase credentials

SUPABASE_URL = "https://rmzvhvucmkyfuyuobuxu.supabase.co" SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJtenZodnVjbWt5ZnV5dW9idXh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQwNDkyMzEsImV4cCI6MjA1OTYyNTIzMX0.LQgMxCWORLt8LiN-9J3-mmshQdOcEaevHqwLhWnJKPA"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

Page configuration

st.set_page_config(page_title="Login", page_icon=":key:", layout="centered")

Theme toggle

if "theme" not in st.session_state: st.session_state.theme = "Light"

theme_toggle = st.radio("Choose Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "Light" else 1)

if theme_toggle != st.session_state.theme: st.session_state.theme = theme_toggle st.rerun()

Apply theme

if st.session_state.theme == "Dark": st.markdown(""" <style> body { background-color: #0e1117; color: white; } .stButton>button { background-color: #262730; color: white; } </style> """, unsafe_allow_html=True)

Title

st.title("Login with Google")

Username input

username = st.text_input("Choose a username")

Google login simulation (Streamlit doesn't support full OAuth with Google directly)

if st.button("Login with Google"): if username.strip() == "": st.warning("Please enter a username before logging in.") else: # Store the username in session state st.session_state.username = username st.success("Logged in successfully!") st.switch_page("home.py")

Footer

st.markdown(""" <hr style='margin-top: 3rem; margin-bottom: 1rem;'> <p style='text-align: center; color: gray;'>Made with love by Hossein</p> """, unsafe_allow_html=True)

