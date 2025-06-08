import streamlit as st
import numpy as np
import joblib
import os

# Define model and vectorizer in the global scope, initialized to None
model = None
tfidf_vectorizer = None

# Define the file paths
model_path = "c:/Users/Jatin/OneDrive/Desktop/PROJECT/SMS_Spam/lrmodel.pkl"
vectorizer_path = "c:/Users/Jatin/OneDrive/Desktop/PROJECT/SMS_Spam/cvmodel.pkl"

# Debugging: Print the paths and check if files exist
# st.write(f"Model path: {model_path}")
# st.write(f"Vectorizer path: {vectorizer_path}")
# st.write(f"Model exists: {os.path.exists(model_path)}")
# st.write(f"Vectorizer exists: {os.path.exists(vectorizer_path)}")
# st.write(f"Current working directory: {os.getcwd()}")

# Load the model and vectorizer
try:
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}")
    else:
        model = joblib.load(model_path)

    if not os.path.exists(vectorizer_path):
        st.error(f"Vectorizer file not found at {vectorizer_path}")
    else:
        tfidf_vectorizer = joblib.load(vectorizer_path)

except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    model = None
    tfidf_vectorizer = None


def show_predict_page():
    st.title("SMS Spam Prediction")
    st.write("Enter the SMS message to check if it's spam or not.")

    # Input field
    sms_text = st.text_area("Enter SMS message", "Type here...")

    # Predict button
    if st.button("Predict"):
        if model is not None and tfidf_vectorizer is not None:
            # Preprocess the input text
            processed_text = [sms_text]
            text_vectorized = tfidf_vectorizer.transform(processed_text)

            # Make prediction
            prediction = model.predict(text_vectorized)[0]

            # Display result
            if prediction == 1:
                st.error("This SMS is predicted as SPAM!")
            else:
                st.success("This SMS is predicted as NOT SPAM.")
        else:
            st.error("Model or vectorizer not loaded. Please check the file paths.")