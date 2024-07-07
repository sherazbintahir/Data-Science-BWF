
# Hi, This is Sheraz Bin Tahir. i made a TO DO LIST PROGRAM as my Mini Project. 
# In this Program we can do following Functions
# 1. Add Task  
# 2. View Task 
# 3. Remove Task 
# 4. Exit




todo_list = []

def add_task(task):
    """Add a new task to the To-Do List."""
    todo_list.append(task)
    print("Added task:", task)

def view_tasks():
    """View all tasks in the To-Do List."""
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(i, ".", task)

def remove_task(task_number):
    """Remove a task from the To-Do List by its number."""
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print("Removed task:", removed_task)
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the To-Do List program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
