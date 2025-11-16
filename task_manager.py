tasks = ["купить хлеб", "позвонить маме"]
task_status = {
    "купить хлеб": "не сделано",
    "позвонить маме": "в процессе"
}

# Добавление задачи
def add_task(task, status="не сделано"):
    tasks.append(task)
    task_status[task] = status

add_task("сделать ДЗ")
print("Задачи:", tasks)
print("Статусы:", task_status)
