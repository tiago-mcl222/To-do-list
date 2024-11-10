tasks = []

def add_task():
    #add task to the list
    task = input("Enter a new task:")
    tasks.append({"description": task, "completed": False})
    print(f"Task {task} added!")


def view_task():
    if not tasks:
        print("No tasks available")
    else:
        print("\nYour to do list:")
        for i in range(len(tasks)):
            if tasks[i]["completed"]:
                status = "Complete"
            else:
                status = "Incomplete"
            print(f"{i+1}.{tasks[i]['description']} - {status}")
            




def task_complete():

    view_task()

    if not tasks:
        return

    select_task = (input("Select the number of the task you want to mark as complete."))

    if not select_task.isdigit():
        print("please enter a valid number.")

        
    task_index = int(select_task) - 1

    if task_index >= 0 and  task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['description']}' marked as complete")
    else:
        print("Invalid task number.")    

    
def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Exit")

        choice = input("Chose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            task_complete()
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        


