import streamlit as st

st.title("📝 To-Do List")

# makes list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task")
# when button is clicked and text isnt empty
if st.button("➕ Add Task") and new_task:
    st.session_state.tasks.append(new_task)
    st.success(f"Added: {new_task}")

# if there are tasks, show them
if st.session_state.tasks:
    st.subheader("Your Tasks")
    # numbers each task, starting at 1
    for i, task in enumerate(st.session_state.tasks, start=1):
        st.write(f"{i}. {task}")
else:
    st.info("No tasks yet. Add one above!")
