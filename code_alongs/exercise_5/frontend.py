import streamlit as st
import requests

prompt = st.text_input("Name a location: ")

if st.button("Recommend restaurant"):
    r = requests.post(
        "http://127.0.0.1:8000/restaurant_recommendation",
        json={"prompt": prompt}
        )
    
    if r.status_code == 200:
        st.success("Restaurant created. Press 'Show restaurants' to show all recommendations.")
    else:
        st.error(f"Something wrong. Code: {r.status_code}")
        st.text(r.text)

if st.button("Show restaurants"):
    r = requests.get("http://127.0.0.1:8000/show_table")
    st.dataframe(r.json())