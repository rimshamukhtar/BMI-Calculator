import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

# Function to get BMI category and health tips
def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight 😔", "Eat nutrient-rich foods, increase protein intake, and exercise regularly."
    elif 18.5 <= bmi < 24.9:
        return "Healthy Weight ✅", "Great job! Keep a balanced diet and stay active. 💪"
    elif 25 <= bmi < 29.9:
        return "Overweight ⚠️", "Consider healthy eating habits and increase physical activity."
    else:
        return "Obese ❌", "Consult a doctor, focus on diet control, and start a workout plan."

# Custom Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #74ebd5, #acb6e5);
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background: linear-gradient(to right, #74ebd5, #acb6e5);
    }
    .main-title {
        text-align: center;
        font-size: 34px;
        font-weight: bold;
        color: white;
        padding: 10px;
        border-radius: 10px;
    }
    .bmi-box {
        padding: 20px;
        background: white;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        text-align: center;
        margin-top: 20px;
    }
    .bmi-value {
        font-size: 28px;
        font-weight: bold;
        color: #007bff;
    }
    .emoji {
        font-size: 28px;
        font-weight: bold;
    }
    .tips {
        font-size: 16px;
        font-weight: bold;
        color: #444;
        margin-top: 10px;
    }
    .stNumberInput, .stButton button {
        font-size: 18px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>💪 BMI Calculator with Health Tips</h1>", unsafe_allow_html=True)

# User Input
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.5, format="%.2f")

# Calculate Button
if st.button("Calculate BMI", key="calculate_btn"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category, tip = get_bmi_status(bmi)

        # Display Results
        st.markdown(f"""
            <div class='bmi-box'>
                <h2>Your BMI: <span class="bmi-value">{bmi}</span></h2>
                <h3 class="emoji">{category}</h3>
                <p class="tips">💡 {tip}</p>
            </div>
        """, unsafe_allow_html=True)

        # Animated Progress Bar
        progress = min(bmi / 40, 1.0)
        st.progress(progress)

    else:
        st.error("Please enter valid values for weight and height!")
