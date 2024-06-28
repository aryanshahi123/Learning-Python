todos = []

total_todos = int(input("Enter total number of todo:"))

for i in range(total_todos):
    todo = input(f"Enter todo{i}")
    todos.append(todo)

print("\n-------------------")
print("All todos are:")

for todo in todos:
    print(todo)