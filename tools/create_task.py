import requests

URL = "http://127.0.0.1:5000/tasks"

def create_task(summary, description):
    new_task = {
        "summary": summary,
        "description": description
    }
    response = requests.post(URL, json=new_task)
    if response.status_code == 201:
        print("Task successfully created1")
    else:
        print("Something went wronwhile trying to create task.")

if __name__ == "__main__":
    create_task("Test my service","Validate the system works")