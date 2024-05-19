class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description, "status": "not completed"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "Completed"
                print(f"Task {description} completed")
            else:
                print(f"Task {description} not found")

    def show_tasks(self):
        print("current tasks")
        for task in self.tasks:
            if task['status'] == "not completed":
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task("01.06.2023", "Read the book")
t.add_task("05.06.2023", "Run the marathon")
t.add_task("27.06.2023", "Fix the car")

t.show_tasks()

t.complete_tasks("Read the book")