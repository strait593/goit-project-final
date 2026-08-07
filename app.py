import streamlit as st
import pickle

def load_model():
    with open('model_logistic.pkl', 'rb') as f:
        model = pickle.load(f)

    return model

model = load_model()

def parse_user_data():
    user_data = {}

    tv_sub = st.selectbox("Does the user posses a TV Subscription?", options=['Yes', 'No'])
    movie_sub = st.selectbox("Does the user posses a Movie Package Subscription?", options=['Yes', 'No'])
    sub_age = float(st.number_input("How old is the user's subscirption?(years)", min_value=0.0, max_value=12.0))
    avg_bil = float(st.number_input("User's average bill",min_value=0, max_value=100))
    rem_contract = st.number_input("Remaining time of user's contract", min_value=0, max_value=3)
    