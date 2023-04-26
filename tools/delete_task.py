# resp = requests.delete(myurl)
import requests

URL = "http://127.0.0.1:5000/tasks"

def delete_task(summary, description):
    new_task = {
        "summary": summary,
        "description": description
    }
    response = requests.delete(URL, json=new_task)
    if response.status_code == 201:
        print("Task successfully deleted!")
    else:
        print("Something went wrong while trying to delete task.")

if __name__ == "__main__":
    print("Testing DEL /tasks")
    print("---------------------")
    delete_task("Test my service","Validate the system works")