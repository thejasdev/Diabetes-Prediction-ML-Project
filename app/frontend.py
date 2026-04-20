import numpy as np
import pickle
import streamlit as st

# Load trained model (use relative path)
loaded_model = pickle.load(open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Diabites ML Project\\training model.sav", "rb"))

# Prediction function
def diabetes_prediction(input_data):
    input_data = np.asarray(input_data)
    input_data = input_data.reshape(1, -1)

    prediction = loaded_model.predict(input_data)

    if prediction[0] == 0:
        return "✅ The Person is Not Diabetic"
    else:
        return "⚠️ The Person is Diabetic"

# Main function
def main():

    # Title
    st.title("🩺 Diabetes Prediction Web App")

    st.write("Enter the patient's medical details below:")

    # Input fields (number_input = BEST practice)
    Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    Glucose = st.number_input("Glucose Level", min_value=0.0)
    BloodPressure = st.number_input("Blood Pressure", min_value=0.0)
    SkinThickness = st.number_input("Skin Thickness", min_value=0.0)
    Insulin = st.number_input("Insulin Level", min_value=0.0)
    BMI = st.number_input("BMI", min_value=0.0)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    Age = st.number_input("Age", min_value=0, step=1)

    diagnosis = ""

    # Button
    if st.button("🔍 Diabetes Test Result"):

        input_data = [
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age
        ]

        diagnosis = diabetes_prediction(input_data)

    # Show result
    if diagnosis:
        st.success(diagnosis)

# Run app
if __name__ == '__main__':
    main()