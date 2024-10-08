# task_manager.py

from task import create_task, mark_task_completed, task_str

def add_task(task_list, description):
    task = create_task(description)
    task_list.append(task)

def list_tasks(task_list):
    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task_str(task)}")

def mark_task_completed_by_index(task_list, index):
    if 0 <= index < len(task_list):
        mark_task_completed(task_list[index])

def clear_completed_tasks(task_list):
    return [task for task in task_list if not task['completed']]