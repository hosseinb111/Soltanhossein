import streamlit as st from supabase import create_client, Client import os

Supabase credentials

url = "https://rmzvhvucmkyfuyuobuxu.supabase.co" key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJtenZodnVjbWt5ZnV5dW9idXh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQwNDkyMzEsImV4cCI6MjA1OTYyNTIzMX0.LQgMxCWORLt8LiN-9J3-mmshQdOcEaevHqwLhWnJKPA" supabase: Client = create_client(url, key)

st.set_page_config(page_title="Home Page", layout="centered")

Theme toggle

if 'theme' not in st.session_state: st.session_state.theme = 'light'

toggle = st.toggle("Dark mode") if toggle: st.session_state.theme = 'dark' else: st.session_state.theme = 'light'

if st.session_state.theme == 'dark': st.markdown(""" <style> body { background-color: #0e1117; color: white; } </style> """, unsafe_allow_html=True) else: st.markdown(""" <style> body { background-color: white; color: black; } </style> """, unsafe_allow_html=True)

Greeting

st.title("Welcome!")

Display user info from session

if 'username' in st.session_state: st.write(f"Logged in as: {st.session_state['username']}") else: st.warning("You are not logged in.")

Fetch example data from Supabase

st.subheader("Data from Supabase:") try: data = supabase.table("profiles").select("*").limit(5).execute() if data.data: for row in data.data: st.json(row) else: st.info("No data found.") except Exception as e: st.error(f"Error fetching data: {e}")

Footer

st.markdown("""

<p style='text-align: center;'>Made with love by Hossein</p>
""", unsafe_allow_html=True)