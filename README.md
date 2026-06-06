# 🚚 Food Delivery Time Prediction

A Machine Learning project that predicts food delivery time based on factors such as distance, preparation time, weather conditions, traffic levels, courier experience, vehicle type, and time of day.

This project includes:

* Data Cleaning & Exploratory Data Analysis (EDA)
* Linear Regression Model Training
* Model Evaluation
* Streamlit Web Application for Predictions

## 📌 Project Overview

The goal of this project is to estimate delivery time for food orders using historical delivery data. By analyzing various factors affecting delivery performance, the model predicts the expected delivery duration.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Pickle

## 📂 Project Structure

```text
Food_Delivery_Pred/
│
├── Food_Delivery_Times.csv      # Dataset
├── LinearRegression2.ipynb      # EDA & Model Training
├── delivery_model.pkl           # Trained Model
├── app.py                       # Streamlit Application
├── README.md
```

## 📊 Features Used

* Distance (km)
* Preparation Time (minutes)
* Courier Experience (years)
* Weather Conditions
* Traffic Level
* Time of Day
* Vehicle Type

## 🤖 Machine Learning Model

Algorithm Used:

* Linear Regression

Workflow:

1. Data Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Encoding
4. Model Training
5. Model Evaluation
6. Model Deployment using Streamlit

## 🚀 Running the Project

### 1. Clone Repository

```bash
git clone https://github.com/kuldeepin3/Food_Delivery_Pred.git
cd Food_Delivery_Pred
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
streamlit run app.py
```

## 🎯 Application Preview

The Streamlit application allows users to:

* Enter delivery details
* Select weather conditions
* Choose traffic level
* Select vehicle type
* Predict delivery time instantly

## 📈 Future Improvements

* Try advanced models like Random Forest and XGBoost
* Hyperparameter tuning
* Model comparison dashboard
* Deployment on Streamlit Cloud
* Real-time delivery tracking integration

## 👨‍💻 Author

**Kuldeep Kirit Prajapati**

* LinkedIn: https://www.linkedin.com/in/kuldeep-prajapati-a929a32ab
* GitHub: https://github.com/kuldeepin3

## ⭐ If you like this project

Give this repository a star and share your feedback!
