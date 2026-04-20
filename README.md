# 🩺 Diabetes Prediction Web App using Machine Learning

## 📌 Project Overview

This project is an end-to-end Machine Learning application that predicts whether a person is diabetic or not based on key medical attributes.

The solution integrates:

* A trained Machine Learning model
* A user-friendly web interface built using Streamlit
* Real-time prediction system

---

## 🎯 Objective

To develop a predictive system that:

* Analyzes patient health data
* Predicts diabetes risk
* Provides an easy-to-use interface for users

---

## 🧠 How It Works

1. User enters medical details in the web app
2. Input data is converted into NumPy array
3. Data is reshaped for model compatibility
4. Pre-trained ML model makes prediction
5. Result is displayed as:

   * ✅ Not Diabetic
   * ⚠️ Diabetic

---

## 📊 Input Features

The model uses the following medical parameters:

* Number of Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin Level
* Body Mass Index (BMI)
* Diabetes Pedigree Function
* Age

---

## ⚙️ Tech Stack

### 💻 Programming

* Python

### 📚 Libraries Used

* NumPy
* Pandas
* Scikit-learn
* Pickle

### 🌐 Web Framework

* Streamlit

---

## 🔄 Project Workflow

1. Data Collection (Diabetes dataset)
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Model Saving using Pickle
7. Web App Development using Streamlit

---

## 🤖 Machine Learning Model

A classification model is trained to predict diabetes outcome based on input features.

The trained model is saved as:

```
training model.sav
```

---

## 🖥️ Application Interface

The Streamlit app provides:

* Input fields for medical data
* Prediction button
* Instant result display

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/thejasdev/Diabites_ML_Project.git
cd Diabites_ML_Project
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
streamlit run frontend.py
```

---

## 📁 Project Structure

```
Diabetes-Prediction-ML-Project/
│
├── app/
│   └── frontend.py              # Streamlit app
│
├── model/
│   └── training_model.sav       # Trained ML model
│
├── data/
│   └── diabetes.csv             # Dataset
│
├── notebooks/
│   └── ml.ipynb                 # Training notebook
│
├── requirements.txt
├── README.md
└── .gitignore

 ```
---

## 📈 Expected Output

* **"The Person is Not Diabetic"**
* **"The Person is Diabetic"**

---

## 💡 Future Improvements

* Improve UI/UX design
* Add data validation
* Deploy on cloud (AWS / Render / Streamlit Cloud)
* Add multiple disease prediction
* Improve model accuracy with advanced algorithms

---

## 📚 Learning Outcomes

* End-to-end Machine Learning pipeline
* Model deployment using Streamlit
* Handling real-world medical dataset
* Building interactive web applications

---

## 👨‍💻 Author

**Thejas K S**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
