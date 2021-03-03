from todo_list.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        current_task = [t for t in self.tasks if t.name == task_name]
        if current_task:
            task = current_task[0]
            task.completed = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    #def clean_section(self):
    #    cleared_tasks = 0
    #    for i in range(len(self.tasks), -1, -1):
    #        if self.tasks[i].completed == True:
    #            self.tasks.pop(i)
    #            cleared_tasks += 1
    #    return f"Cleared {cleared_tasks} tasks."

    def clean_section(self):
        all_not_completed_tasks = [t for t in self.tasks if not t.completed]
        removed_tasks = len(self.tasks) - len(all_not_completed_tasks)
        self.tasks = all_not_completed_tasks
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for task in self.tasks:
            res += task.details() + "\n"
        return res

#task = Task("Make bed", "27/05/2020")
#print(task.change_name("Go to University"))
#print(task.change_due_date("28.05.2020"))
#task.add_comment("Don't forget laptop")
#print(task.edit_comment(0, "Don't forget laptop and notebook"))
#print(task.details())
#section = Section("Daily tasks")
#print(section.add_task(task))
#second_task = Task("Make bed", "27/05/2020")
#section.add_task(second_task)
#print(section.clean_section())
#print(section.view_section())