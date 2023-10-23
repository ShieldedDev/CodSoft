# Function to add a task to the to-do list
def add_task(to_do_list, task):
    to_do_list.append(task)

# Function to view the to-do list
def view_tasks(to_do_list):
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# Function to remove a task from the to-do list
def remove_task(to_do_list, task_index):
    if 1 <= task_index <= len(to_do_list):
        removed_task = to_do_list.pop(task_index - 1)
        return removed_task
    else:
        return None

# Function to save the to-do list to a file
def save_to_do_list(to_do_list):
    with open("to_do_list.txt", "w") as file:
        for task in to_do_list:
            file.write(task + "\n")

# Function to load the to-do list from a file
def load_to_do_list():
    to_do_list = []
    try:
        with open("to_do_list.txt", "r") as file:
            for line in file:
                to_do_list.append(line.strip())
    except FileNotFoundError:
        pass
    return to_do_list

# Main program
to_do_list = load_to_do_list()

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Save and Quit")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        task = input("Enter a task: ")
        add_task(to_do_list, task)
        print("Task added to the to-do list.")
    elif choice == '2':
        view_tasks(to_do_list)
    elif choice == '3':
        view_tasks(to_do_list)
        if not to_do_list:
            print("There are no tasks to remove.")
            continue
        try:
            task_index = int(input("Enter the number of the task to remove: "))
            removed_task = remove_task(to_do_list, task_index)
            if removed_task:
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")
    elif choice == '4':
        save_to_do_list(to_do_list)
        print("To-do list saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
