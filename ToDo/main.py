from todo import Todo

all_todos = []

def display_todo():
    for todo in all_todos:
        print(f"Title: {todo.title}, Description:{todo.desc}")

t1 = Todo("Go To Gym", "For healthier body")
t2 = Todo("Learn Python", "To move in career")

all_todos.append(t1)
all_todos.append(t2)
display_todo()