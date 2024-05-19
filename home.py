class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task: {self.description}, Deadline: {self.deadline}, Completed: {self.completed}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                break

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __str__(self):
        task_list = "\n".join(str(task) for task in self.tasks)
        return f"Task Manager:\n{task_list}"

# Пример использования
task1 = Task("Finish home task", "20.05.2024")
task2 = Task("Buy groceries", "18.05.2024")
task3 = Task("Call wife", "19.05.2024")

manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)

print("Initial Tasks:")
print(manager)

manager.mark_task_completed("Buy groceries")

print("\nTasks after marking 'Buy groceries' as completed:")
print(manager)

print("\nPending Tasks:")
for task in manager.get_pending_tasks():
    print(task)