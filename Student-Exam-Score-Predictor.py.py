import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

import pandas as pd

# Create sample dataset
data = pd.DataFrame({
    'StudyHours': [2, 4, 5, 3, 6, 8, 1, 7],
    'SleepHours': [7, 6, 8, 7, 5, 6, 8, 5],
    'Score': [55, 65, 78, 60, 85, 90, 50, 88]
})

# Save dataset as Excel
data.to_excel("student_scores.xlsx", index=False)  # Creates the file
print("Excel file saved successfully!")


# Train the model
X = data[['StudyHours', 'SleepHours']]
y = data['Score']
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("📚 Student Exam Score Predictor")
st.write("Adjust the sliders to predict your score based on study & sleep hours.")

# User input sliders
study_hours = st.slider("Study Hours per day", 0, 10, 5)
sleep_hours = st.slider("Sleep Hours per day", 0, 10, 6)

# Prediction
input_data = pd.DataFrame([[study_hours, sleep_hours]], columns=["StudyHours", "SleepHours"])
predicted_score = model.predict(input_data)[0]

# Output
st.subheader(f"Predicted Score: {predicted_score:.2f}%")
st.write("📌 Tip: Aim for **5–7 hours study** and **6–7 hours sleep** for better results.")

# Show dataset
with st.expander("See training dataset"):
    st.dataframe(data)
