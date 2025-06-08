# SMS Spam Detector 📩

This project is a machine learning-based SMS spam detector that classifies messages as either "spam" or "ham." The model is built using Logistic Regression and is deployed as a web application with Streamlit.

## ✨ Features

* **Real-time Classification:** Instantly classify SMS messages to identify and filter out spam.
* **High Precision:** The model is optimized for high precision to minimize false positives, ensuring that important messages are not mistakenly marked as spam.
* **Interactive Web App:** A user-friendly interface built with Streamlit that allows for easy interaction and testing of the model.
* **Data-driven:** Trained on a dataset of SMS messages with extensive preprocessing to enhance accuracy.

## 🛠️ Built With

* **Python** - The core programming language.
* **Scikit-learn** - For building the Logistic Regression model and data preprocessing.
* **Pandas** - For data manipulation and analysis.
* **Streamlit** - To create and deploy the interactive web application.
* **NLTK** - For natural language processing tasks.
* **Pickle** - For saving and loading the trained model.

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You need to have Python and pip installed on your machine.

### Installation

1.  Clone the repo
    ```sh
    git clone [https://github.com/your_username/sms-spam-detector.git](https://github.com/your_username/sms-spam-detector.git)
    ```
2.  Install the required packages
    ```sh
    pip install -r requirements.txt
    ```
3.  Run the Streamlit app
    ```sh
    streamlit run app.py
    ```

### Usage

1.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
2.  Enter an SMS message in the text box.
3.  Click the "Predict" button to see the classification.

## 📈 Model Performance

The model was evaluated on a test set and achieved the following performance metrics:

* **Accuracy:** 97.6%
* **Precision:** 98.3%

This high precision ensures that the model is highly reliable in identifying spam without incorrectly flagging legitimate messages.
