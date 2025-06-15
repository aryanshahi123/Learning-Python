total_todo = int(input("Enter total todo:"))
todos = []

for i in range(0, total_todo):
    todo = input(f"Enter todo {i+1}:")
    todos.append(todo)

for todo in todos:
    print(todo)

print("Okay")!