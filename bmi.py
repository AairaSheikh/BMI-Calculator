import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("🩺 BMI Calculator")

# --- Inputs ---
age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
height_feet = st.number_input(
    "Height (in feet, e.g. 5.5 for 5′6″)", min_value=0.5, max_value=10.0, value=5.5, step=0.1
)
weight = st.number_input("Weight", min_value=1.0, max_value=999.0, value=70.0, step=0.5)
weight_unit = st.selectbox("Weight unit", ["kg", "lbs"])

# --- Calculate button ---
if st.button("Calculate BMI"):
    # Convert inputs
    height_m = height_feet * 0.3048
    if weight_unit == "lbs":
        weight_kg = weight * 0.45359237
    else:
        weight_kg = weight

    bmi = weight_kg / (height_m ** 2)
    bmi_value = round(bmi, 2)

    # Optional classification
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    st.subheader("Your Results")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Height:** {height_feet} ft ({height_m:.2f} m)")
    st.write(f"**Weight:** {weight} {weight_unit} ({weight_kg:.2f} kg)")
    st.metric(label="BMI", value=bmi_value)
    st.write(f"**Status:** {status}")
