import pandas as pd
import json
import os

class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

def save_new_entry(entries, ids_list, sum_of_ages):
    name = input("Please enter a name: ")
    id_number = get_number_only("Please enter the ID of the name (numbers only): ")

    if id_number in entries:
        print("ID " + id_number + " already exists.")
        return entries, ids_list, sum_of_ages

    age = int(get_number_only("Please enter the age: "))
    person = Person(name, age, id_number)
    entries[id_number] = person
    ids_list.append(id_number)
    sum_of_ages += age
    return entries, ids_list, sum_of_ages

def search_by_id(entries):
    id_number = get_number_only("Please enter the ID to search for (numbers only): ")
    if id_number in entries:
        print_user_by_id(entries[id_number])
    else:
        print("The record with ID " + id_number + " does not exist in the system.")

def print_ages_average(entries, sum_of_ages):
    if len(entries) == 0:
        print("No entries to calculate the average age.")
    else:
        average_age = sum_of_ages / len(entries)
        print("The average age is: " + str(average_age))

def print_all_names(entries):
    if not entries:
        print("No entries found.")
        return
    for entry in entries.values():
        print(entry.name)

def print_all_ids(entries):
    if not entries:
        print("No entries found.")
        return
    for id_number in entries:
        print(id_number)

def print_all_entries(entries):
    if not entries:
        print("No entries found.")
        return
    for id_number, person in entries.items():
        print_user_by_id(person)

def print_entry_by_index(ids_list, entries):
    if not entries:
        print("No entries found.")
        return
    index = int(get_number_only("Please enter the index (numbers only): "))
    if index < 0 or index >= len(ids_list):
        print("Index out of range. Maximum allowed index is: " + str(len(ids_list) - 1))
    else:
        id_number = ids_list[index]
        print_user_by_id(entries[id_number])

def want_to_leave():
    while True:
        confirmation = input("Are you sure you want to exit? (y/n): ").lower()
        if confirmation == "y":
            print("Bye bye, have a nice day :)")
            exit()
        elif confirmation == "n":
            return

def save_all_data(entries):
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
            column_names["id"]: person.id_number,
            column_names["name"]: person.name,
            column_names["age"]: person.age
        })

    df = pd.DataFrame(data_saving)
    full_output_path = os.path.join(current_path, output_file)
    df.to_csv(full_output_path, index=False)
    print("Data saved successfully to: " + full_output_path)

def get_number_only(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        else:
            print("Invalid input. Please enter numbers only.")

def print_user_by_id(person):
    print("ID: " + person.id_number + ", Name: " + person.name + ", Age: " + str(person.age))

def print_menu():
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
        print_menu()
        choice = get_number_only("Please enter your choice (1-9): ")

        if choice == "1":
            entries, ids_list, sum_of_ages = save_new_entry(entries, ids_list, sum_of_ages)
        elif choice == "2":
            search_by_id(entries)
        elif choice == "3":
            print_ages_average(entries, sum_of_ages)
        elif choice == "4":
            print_all_names(entries)
        elif choice == "5":
            print_all_ids(entries)
        elif choice == "6":
            print_all_entries(entries)
        elif choice == "7":
            print_entry_by_index(ids_list, entries)
        elif choice == "8":
            save_all_data(entries)
        elif choice == "9":
            want_to_leave()
        input("Press Enter to continue...")

# The start is here!
print("Our software helps you make a list of people's info to keep things organized. (Name, ID, and age)")
menu()