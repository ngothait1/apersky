import pandas as pd
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
    person_types = [Student, Employee, Person]

    while True:
        person_type = input("Is this person a (0) Student, (1) Employee, or (2) Neither? ")
        
        if person_type in ["0", "1", "2"]:
            person_class = person_types[int(person_type)]
            person = person_class(name, age, id_number)
            break
        else:
            print("Invalid option. Please choose 0, 1, or 2.")

    entries[id_number] = person
    ids_list.append(id_number)
    sum_of_ages += age
    return entries, ids_list, sum_of_ages

def searchById(entries):
    id_number = getNumberOnly("Please enter the ID to search for (numbers only): ")
    person = entries.get(id_number)
    if person:
        person.printMyself()
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
        entries[id_number].printMyself()
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
    output_file = input("What is your output file name? ")
    if not output_file.endswith(".csv"):
        output_file += ".csv"

    data_saving = []
    for person in entries.values():
        data_saving.append(person.getInfoDict())

    df = pd.DataFrame(data_saving)
    df.to_csv(output_file, index=False)
    print("Data saved successfully to:", output_file)

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