import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="Student Progress Bot", layout="wide")

st.title("📊 Student Performance Progress BOT")

# Load data
data = pd.read_csv("student_data.csv")
data['Date'] = pd.to_datetime(data['Date'])

# Sidebar
st.sidebar.header("Select Student Details")

student_id = st.sidebar.selectbox(
    "Student ID",
    sorted(data["StudentID"].unique())
)

student_data = data[data["StudentID"] == student_id]

subject = st.sidebar.selectbox(
    "Subject",
    student_data["Subject"].unique()
)

subject_data = student_data[student_data["Subject"] == subject]

# -------- Line Chart --------
st.subheader(f"📈 Progress Trend - {subject}")

plt.figure(figsize=(8, 4))
plt.plot(subject_data["Date"], subject_data["Score"], marker='o')
plt.xlabel("Date")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)


# -------- Bar Chart --------
st.subheader("📊 Subject-wise Average Comparison")

avg_scores = student_data.groupby("Subject")["Score"].mean()

plt.figure()
avg_scores.plot(kind="bar")
plt.ylabel("Average Score")
plt.grid(axis='y')
st.pyplot(plt)

# -------- Prediction --------
st.subheader("🔮 Future Performance Prediction")

X = np.array(range(len(subject_data))).reshape(-1, 1)
y = subject_data["Score"].values

model = LinearRegression()
model.fit(X, y)

future_test = np.array([[len(subject_data)]])
prediction = model.predict(future_test)

st.success(f"Predicted Next Score in {subject}: {round(prediction[0], 2)}")