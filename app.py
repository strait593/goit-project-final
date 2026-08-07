import streamlit as st
import pickle
import pandas as pd

def load_model():
    with open('model_logistic.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

def parse_user_data() -> dict:
    is_tv_subscriber = st.selectbox("Does the user posses a TV Subscription?(1: Yes; 0:No)", options=[0, 1])
    is_movie_package_subscriber = st.selectbox("Does the user posses a Movie Package Subscription?(1: Yes; 0:No)", options=[0, 1])
    subscription_age = float(st.number_input("How old is the user's subscirption?(years)", min_value=0.0, max_value=12.0))
    bill_avg = float(st.number_input("User's average bill",min_value=0, max_value=100))
    reamining_contract = st.number_input("Remaining time of user's contract", min_value=0, max_value=3)
    is_missing_contract = st.selectbox("Does the user have a missing contract(1: Yes; 0:No)", options=[0, 1])
    service_failure_count = st.number_input("The amount of times the user has encountered a service failure", min_value=0, max_value=15)
    download_avg = st.number_input("Amount of user's downloads", min_value=0, max_value=4500)
    upload_avg = st.number_input("Amount of user's uploads", min_value=0, max_value=460)
    download_over_limit = st.number_input("Amount of user's downloads that went off limit", min_value=0, max_value=10)

    return {
        "is_tv_subscriber": is_tv_subscriber,
        "is_movie_package_subscriber": is_movie_package_subscriber,
        "subscription_age": subscription_age,
        "bill_avg": bill_avg,
        "reamining_contract": reamining_contract,
        "is_missing_contract":is_missing_contract,
        "service_failure_count": service_failure_count,
        "download_avg": download_avg,
        "upload_avg": upload_avg,
        "download_over_limit": download_over_limit
    }


def make_prediction(user_data: dict) -> tuple[float, str]:
    data = pd.DataFrame([user_data])
    pred = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    decision = "The customer has a high chance of cancelling Their subscription" if pred == 1 else "The customer has a high chance of keeping Their subscription"

    return probability, decision

def main():
    st.title("Customer churn Predictor")
    user_data = parse_user_data()

    if st.button("Predict"):
        probability, decision = make_prediction(user_data)
        st.subheader("Prediction result")
        st.write(f"Churn probability: {probability * 100:.1f}%")
        st.write(f"Decision: {decision}")

if __name__ == "__main__":
    main()