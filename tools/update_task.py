# To issue a put request via requests
# resp = requests.put("URL", json=mydata)
import requests

URL = "http://127.0.0.1:5000/tasks"

def update_task(summary, description):
    new_task = {
        "summary": summary,
        "description": description
    }
    response = requests.put(URL, json=new_task)
    if response.status_code == 201:
        print("Task successfully updated!")
    else:
        print("Something went wrong while trying to update task.")

if __name__ == "__main__":
    print("Testing UPDATE /tasks")
    print("---------------------")
    update_task("Test my service","Validate the system works")