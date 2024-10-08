# task.py

def create_task(description):
    return {'description': description, 'completed': False}

def mark_task_completed(task):
    task['completed'] = True

def task_str(task):
    status = "✓" if task['completed'] else "✗"
    return f"[{status}] {task['description']}"