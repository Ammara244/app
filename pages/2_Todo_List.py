import streamlit as st

st.title("📝 To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task")
if st.button("➕ Add Task") and new_task:
    st.session_state.tasks.append(new_task)
    st.success(f"Added: {new_task}")

if st.session_state.tasks:
    st.subheader("Your Tasks")
    for i, task in enumerate(st.session_state.tasks, start=1):
        st.write(f"{i}. {task}")
else:
    st.info("No tasks yet. Add one above!")
