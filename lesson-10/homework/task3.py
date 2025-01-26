import json
import csv

def load_tasks():
    with open('tasks.json', 'r') as f:
        return json.load(f)

def display_tasks(tasks):
    print("\nAll Tasks:")
    print("ID | Task Name         | Completed | Priority")
    print("---------------------------------------------")
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:17} | {str(task['completed']):9} | {task['priority']}")

def calculate_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    avg_priority = sum(t['priority'] for t in tasks) / total
    avg_priority = round(avg_priority, 1)
    return {
        'total_tasks': total,
        'completed_tasks': completed,
        'pending_tasks': pending,
        'average_priority': avg_priority
    }

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)
    print("\nTasks saved to tasks.json")

def convert_to_csv(tasks):
    with open('tasks.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
    print("Tasks converted to tasks.csv")

if __name__ == '__main__':
    tasks = load_tasks()
    display_tasks(tasks)
    
    stats = calculate_statistics(tasks)
    print("\nTask Statistics:")
    print(f"Total tasks: {stats['total_tasks']}")
    print(f"Completed tasks: {stats['completed_tasks']}")
    print(f"Pending tasks: {stats['pending_tasks']}")
    print(f"Average priority: {stats['average_priority']}")
    
    save_tasks(tasks)
    convert_to_csv(tasks)
