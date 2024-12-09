import requests

SERVER_URL = ""
SERVER_PORT = 80
STUDENT_API = "students"

def getStudentsFullUrl():
    return SERVER_URL + "/" + STUDENT_API

def setServerUrlAndPort(ip, port):
    global SERVER_URL, SERVER_PORT
    SERVER_PORT = port
    SERVER_URL = "http://" + ip + ":" + str(SERVER_PORT)

def printStudentDetails(student):
    print("ID: " + str(student["id"]))
    print("Name: " + student["name"])
    print("Age: " + str(student["age"]))
    print("--------------------")

def getStudentsList():
    response = requests.get(getStudentsFullUrl())
    if response.status_code == 200:
        students = response.json().get("students", [])
        if students:
            print("\n--- Students List ---")
            for student in students:
                printStudentDetails(student)
        else:
            print("\nNo students found.")
    else:
        print("\nError in students list.")

def getStudentById():
    student_id = input("Enter the student ID: ")
    response = requests.get(getStudentsFullUrl() + "/" + student_id)
    if response.status_code == 200:
        student = response.json()
        print("\n--- Student Information ---")
        printStudentDetails(student)
    elif response.status_code == 404:
        print("\nError: Student not found.")
    else:
        print("\nError in student information.")

def saveNewStudent():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    data = {"name": name, "age": int(age)}
    response = requests.post(getStudentsFullUrl(), json=data)
    if response.status_code == 201:
        print("\nStudent created successfully:")
        student = response.json()
        printStudentDetails(student)
    else:
        print("\nError: Student creation failed.")

def changeStudentName():
    student_id = input("Enter the student ID: ")
    new_name = input("Enter new student name: ")
    response = requests.get(getStudentsFullUrl() + "/" + student_id)
    if response.status_code == 200:
        existing_data = response.json()
        data = {"name": new_name, "age": existing_data["age"]}
        update_response = requests.put(getStudentsFullUrl() + "/" + student_id, json=data)
        if update_response.status_code == 200:
            print("\nStudent name updated successfully.")
        else:
            print("\nError updating student name.")
    elif response.status_code == 404:
        print("\nError: Student not found.")
    else:
        print("\nError retrieving student information.")

def changeStudentAge():
    student_id = input("Enter the student ID: ")
    new_age = input("Enter new student age: ")
    response = requests.get(getStudentsFullUrl() + "/" + student_id)
    if response.status_code == 200:
        existing_data = response.json()
        data = {"name": existing_data["name"], "age": int(new_age)}
        update_response = requests.put(getStudentsFullUrl() + "/" + student_id, json=data)
        if update_response.status_code == 200:
            print("\nStudent age updated successfully.")
        else:
            print("\nError updating student age.")
    elif response.status_code == 404:
        print("\nError: Student not found.")
    else:
        print("\nError retrieving student information.")

def deleteStudent():
    student_id = input("Enter the student ID: ")
    response = requests.delete(getStudentsFullUrl() + "/" + student_id)
    if response.status_code == 200:
        print("\nStudent deleted successfully.")
    elif response.status_code == 404:
        print("\nError: Student not found.")
    else:
        print("\nError deleting student.")

def main():
    host_ip = input("Enter the host address: ")
    port = int(input("Enter the port number: "))
    setServerUrlAndPort(host_ip, port)

    while True:
        print("\nWhat do you want to do?")
        print("1. Get students list")
        print("2. Get a specific student information")
        print("3. Save a new student")
        print("4. Change student name")
        print("5. Change student age")
        print("6. Delete student")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            getStudentsList()
        elif choice == "2":
            getStudentById()
        elif choice == "3":
            saveNewStudent()
        elif choice == "4":
            changeStudentName()
        elif choice == "5":
            changeStudentAge()
        elif choice == "6":
            deleteStudent()
        elif choice == "7":
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
