import streamlit as st
import pandas as pd

# Title
st.title("Student Registration Form")

# Form
with st.form("student_form"):
    st.subheader("Enter Student Details")

    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    course = st.selectbox(
        "Course",
        ["Computer Science", "Information Technology", "Electronics", "Mechanical"]
    )
    address = st.text_area("Address")

    submit = st.form_submit_button("Register")

# Form Submission
if submit:
    student_data = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Email": email,
        "Phone": phone,
        "Course": course,
        "Address": address
    }

    st.success("Student Registered Successfully!")
    st.write("### Registered Details")
    st.write(student_data)

    # Convert to DataFrame
    df = pd.DataFrame([student_data])
    st.dataframe(df)