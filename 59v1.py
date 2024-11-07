import pandas as pd
import json
import os
from person import Person
from student import Student
from employee import Employee

def saveNewEntry(entries, ids_list, sum_of_ages):
    name = input("Please enter a name: ")
    id_number = getNumberOnly("Please enter the ID of the name (numbers only): ")

    if id_number in entries:
        print("ID " + id_number + " already exists.")
        return entries, ids_list, sum_of_ages

    age = int(getNumberOnly("Please enter the age: "))

    while True:
        person_type = input("Is this person a (1) Student, (2) Employee, or (3) Neither? ")
        if person_type in ["1", "2", "3"]:
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

    if person_type == "1":
        field_of_study = input("Enter the field of study: ")
        year_of_study = int(getNumberOnly("Enter the year of study: "))
        score_avg = float(input("Enter the average score: "))
        person = Student(name, age, id_number, field_of_study, year_of_study, score_avg)
    elif person_type == "2":
        field_of_work = input("Enter the field of work: ")
        salary = int(input("Enter the salary: "))
        person = Employee(name, age, id_number, field_of_work, salary)
    else:
        person = Person(name, age, id_number)

    entries[id_number] = person
    ids_list.append(id_number)
    sum_of_ages += age
    return entries, ids_list, sum_of_ages

def searchById(entries):
    id_number = getNumberOnly("Please enter the ID to search for (numbers only): ")
    person = entries.get(id_number)
    if person:
        person.printPerson()
    else:
        print("The record with ID " + id_number + " does not exist in the system.")

def printAgesAverage(entries, sum_of_ages):
    if len(entries) == 0:
        print("No entries to calculate the average age.")
    else:
        average_age = sum_of_ages / len(entries)
        print("The average age is: " + str(average_age))

def printAllNames(entries):
    if not entries:
        print("No entries found.")
        return
    for entry in entries.values():
        print(entry.getName())

def printAllIds(entries):
    if not entries:
        print("No entries found.")
        return
    for id_number in entries:
        print(id_number)

def printAllEntries(entries):
    if not entries:
        print("No entries found.")
        return
    for person in entries.values():
        person.printMyself()

def printEntryByIndex(ids_list, entries):
    if not entries:
        print("No entries found.")
        return

    index = getNumberOnly("Please enter the index (numbers only): ")
    index_int = int(index)
    if 0 <= index_int < len(ids_list):
        id_number = ids_list[index_int]
        entries[id_number].printPerson()
    else:
        print("Invalid index. Please enter a number within range.")

def wantToLeave():
    while True:
        confirmation = input("Are you sure you want to exit? (y/n): ").lower()
        if confirmation == "y":
            print("Bye bye, have a nice day :)")
            exit()
        elif confirmation == "n":
            return

def saveAllData(entries):
    config_file = "conf.json"
    current_path = os.getcwd()
    full_config_file = os.path.join(current_path, config_file)

    if not os.path.exists(full_config_file):
        print("Error: Config file [" + config_file + "] is missing in path: " + full_config_file)
        return

    output_file = input("What is your output file name? ")
    if not output_file.endswith(".csv"):
        output_file += ".csv"

    with open(full_config_file) as json_file:
        column_names = json.load(json_file)

    data_saving = []
    for id_number, person in entries.items():
        data_saving.append({
            column_names["id"]: person.getIdNumber(),
            column_names["name"]: person.getName(),
            column_names["age"]: person.getAge()
        })

# if person.getType() == "Student":
# if person.getType() == "Employee":


    df = pd.DataFrame(data_saving)
    full_output_path = os.path.join(current_path, output_file)
    df.to_csv(full_output_path, index=False)
    print("Data saved successfully to: " + full_output_path)

def getNumberOnly(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        else:
            print("Invalid input. Please enter numbers only.")


def printMenu():
    print("Please choose an option:")
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")

def menu():
    entries = {}
    ids_list = []
    sum_of_ages = 0
    while True:
        printMenu()
        choice = getNumberOnly("Please enter your choice (1-9): ")

        if choice == "1":
            entries, ids_list, sum_of_ages = saveNewEntry(entries, ids_list, sum_of_ages)
        elif choice == "2":
            searchById(entries)
        elif choice == "3":
            printAgesAverage(entries, sum_of_ages)
        elif choice == "4":
            printAllNames(entries)
        elif choice == "5":
            printAllIds(entries)
        elif choice == "6":
            printAllEntries(entries)
        elif choice == "7":
            printEntryByIndex(ids_list, entries)
        elif choice == "8":
            saveAllData(entries)
        elif choice == "9":
            wantToLeave()
        input("Press Enter to continue...")

# The start is here!
print("Our software helps you make a list of people's info to keep things organized. (Name, ID, and age)")
menu()
