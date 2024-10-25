import pandas as pd
import json
import os

def saveNewEntry(entries, sum_of_ages, ids_list):
    name = input("Please enter a name: ")
    id_number = getNumberOnly("Please enter the ID of the name (numbers only): ")

    if id_number in entries:
        print("ID " + id_number + " already exists.")
        return sum_of_ages  

    age = int(getNumberOnly("Please enter the age: "))

    entries[id_number] = {"name": name, "age": age}
    ids_list.append(id_number)  
    sum_of_ages += age
    return sum_of_ages

def searchById(entries):
    id_number = getNumberOnly("Please enter the ID to search for (numbers only): ")
    if id_number in entries:
        entry = entries[id_number]
        printUserById(id_number, entry) 
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
        print(entry["name"])

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
    for id_number, entry in entries.items():
        printUserById(id_number, entry)

def printEntryByIndex(entries, ids_list):
    if not entries:
        print("No entries found.")
        return
    index = int(getNumberOnly("Please enter the index (numbers only): "))
    if index < 0 or index >= len(ids_list):
        print("Index out of range. Maximum allowed index is: " + str(len(ids_list) - 1))
    else:
        id_number = ids_list[index]
        entry = entries[id_number]
        printUserById(id_number, entry)

def wantToLeave():
    while True:
        confirmation = input("Are you sure you want to exit? (y/n): ").lower()
        if confirmation == "y":
            print("Bye bye, have a nice day :)")
            exit()
        elif confirmation == "n":
            return  

def getNumberOnly(some_text):
    while True:
        value = input(some_text)
        if value.isdigit():
            return value
        else:
            print("Invalid input. Please enter numbers only.")

def printUserById(id_number, entry):
    print("ID: " + id_number + ", Name: " + entry["name"] + ", Age: " + str(entry["age"]))

def saveAllData(entries):
    config_path = "conf.json"
    current_path = os.getcwd()
    full_config_path = os.path.join(current_path, config_path)

    if not os.path.exists(full_config_path):
        print("Error: Config file '" + config_path + "' is missing in path: " + full_config_path)
        return

    with open(full_config_path) as json_file:
        column_names = json.load(json_file)

    output_file = input("What is your output file name? ")

    data_saving = []
    for id_number, entry in entries.items():
        data_saving.append({
            column_names["id"]: id_number,
            column_names["name"]: entry["name"],
            column_names["age"]: entry["age"]
        })

    df = pd.DataFrame(data_saving)
    full_output_path = os.path.join(current_path, output_file)

    if os.path.exists(full_output_path):
        print("File already exists at: " + full_output_path)
    else:
        df.to_csv(full_output_path, index=False)
        print("Data saved successfully to: " + full_output_path)


def menu():
    entries = {}
    sum_of_ages = 0
    ids_list = []

    while True:
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

        choice = getNumberOnly("Please enter your choice (1-9): ")

        if choice == "1":
            sum_of_ages = saveNewEntry(entries, sum_of_ages, ids_list)
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
            printEntryByIndex(entries, ids_list)
        elif choice == "8":
            saveAllData(entries)
        elif choice == "9":
            wantToLeave()
        input("Press Enter to continue...")

# The start is here!
print("Our software helps you make a list of people's info to keep things organized. (Name, ID, and age)")
menu()
