import streamlit as st
import func_todos

todos = func_todos.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func_todos.write_todos(todos)


st.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func_todos.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a new Todo", placeholder="Enter Todo here...",
              on_change=add_todo, key='new_todo')


