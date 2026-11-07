import streamlit as st
st.title("BMI Calculator")
st.write("Enter your details to calculate your BMI")

weight = st.number_input("Enter your Weight (kg)", min_value=1.0)
height = st.number_input("Enter your height (meters)", min_value=1.0)

if st.button("Calculate BMI"):
    bmi = weight / (height * height)
    st.write("your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.warning("you are underweight")
    elif bmi < 25:
        st.success("you have a normal weight")
    else:
        st.error("you are overweight")

