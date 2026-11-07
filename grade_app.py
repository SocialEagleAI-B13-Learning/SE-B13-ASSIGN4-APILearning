import streamlit as st


def grade_for(mark):
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


if "students" not in st.session_state:
    st.session_state.students = []

st.title("Grade Manager")

with st.form("add_student", clear_on_submit=True):
    name = st.text_input("Student name")
    mark = st.number_input("Mark", value=0.0, step=1.0)
    submitted = st.form_submit_button("Add student")

if submitted:
    if not name.strip():
        st.error("Enter a student name.")
    elif not 0 <= mark <= 100:
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append(
            {"Name": name.strip(), "Mark": mark, "Grade": grade_for(mark)}
        )
        st.success("Student added.")

if st.session_state.students:
    st.subheader("Students")
    st.dataframe(st.session_state.students, hide_index=True)

    marks = [student["Mark"] for student in st.session_state.students]
    average, highest, lowest = st.columns(3)
    average.metric("Class average", f"{sum(marks) / len(marks):.2f}")
    highest.metric("Highest", f"{max(marks):.2f}")
    lowest.metric("Lowest", f"{min(marks):.2f}")
else:
    st.info("Add a student to see results and class figures.")
