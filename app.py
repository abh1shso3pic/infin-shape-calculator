import math
import streamlit as st

# Title and description header
st.title("📐 Shape Area Calculator")
st.write("Select a shape below and enter its dimensions to calculate the area.")

# Dropdown menu to replace the terminal menu options
shape_choice = st.selectbox(
    "Choose a shape:",
    ["Select a Shape", "Circle", "Rectangle", "Square", "Triangle"],
)

# 1. Circle Calculation
if shape_choice == "Circle":
    st.subheader("Circle")
    radius = st.number_input("Enter the radius:", min_value=0.0, step=0.1)

    if st.button("Calculate Area"):
        area = math.pi * radius * radius
        st.success(f"**Area of Circle = {area:.2f}**")

# 2. Rectangle Calculation
elif shape_choice == "Rectangle":
    st.subheader("Rectangle")
    length = st.number_input("Enter the length:", min_value=0.0, step=0.1)
    breadth = st.number_input("Enter the breadth:", min_value=0.0, step=0.1)

    if st.button("Calculate Area"):
        area = length * breadth
        st.success(f"**Area of Rectangle = {area:.2f}**")

# 3. Square Calculation
elif shape_choice == "Square":
    st.subheader("Square")
    side = st.number_input("Enter the side:", min_value=0.0, step=0.1)

    if st.button("Calculate Area"):
        area = side * side
        st.success(f"**Area of Square = {area:.2f}**")

# 4. Triangle Calculation
elif shape_choice == "Triangle":
    st.subheader("Triangle")
    base = st.number_input("Enter the base:", min_value=0.0, step=0.1)
    height = st.number_input("Enter the height:", min_value=0.0, step=0.1)

    if st.button("Calculate Area"):
        area = 0.5 * base * height
        st.success(f"**Area of Triangle = {area:.2f}**")
