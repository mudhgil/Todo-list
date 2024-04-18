#Program to emulate a simple to do list application.

class Todo:
    def __init__(self):
        self.tasks = []

    def add(self, task): # function to add a task
        self.tasks.append(task)
        print(f"{task} has been added")

    def remove(self, task): # function to remove a task
        if task in self.tasks:
            self.tasks.remove(task)
            print("{task} has been removed")
        else:
            print('Task not found!')

    def display(self): # display the list of to do tasks.
        if self.tasks:
            print('Tasks: ')
            for i, task in enumerate(self.tasks, start = 1):
                print(f"{i}, {task}")
        else:
            print('No task added in the list!')

def main():
    to_do = Todo()
    while True:
        print('\nMenu: ')
        print('1. Add task ')
        print('2. Remove the completed task')
        print('3. Display all tasks')
        print('4. Exit the program')
        choice = input('Enter the choice')

        if choice == '1':
            task = input('Add the task: ')
            to_do.add(task)
        elif choice == '2':
            task = input('Type the task you want to delete: ')
            to_do.remove(task)
        elif choice == '3':
            to_do.display()
        elif choice == '4':
            print('Exiting program')
            break
        else:
            print('Invalid choice')
if __name__ == '__main__':
    main()



        