import pandas as pd
import os
from person import Person
from student import Student
from employee import Employee
from utils import getNumberOnly
from enum import Enum, auto

class MenuOption(Enum):
    SAVE_NEW_ENTRY = auto()
    SEARCH_BY_ID = auto()
    PRINT_AGES_AVERAGE = auto()
    PRINT_ALL_NAMES = auto()
    PRINT_ALL_IDS = auto()
    PRINT_ALL_ENTRIES = auto()
    PRINT_ENTRY_BY_INDEX = auto()
    SAVE_ALL_DATA = auto()
    EXIT = auto()

sum_of_ages = 0
entries = {}
ids_list = []
def saveNewEntry():
    global sum_of_ages, entries, ids_list
    name = input("Please enter a name: ")
    id_number = getNumberOnly("Please enter the ID of the name (numbers only): ")

    if id_number in entries:
        print("ID " + id_number + " already exists.")
        
    age = int(getNumberOnly("Please enter the age: "))
    person_types = [Student, Employee, Person]
    index = 0
    for person_type in person_types:
        print("(" + str(index) + ") " + person_type.__name__)
        index += 1

    person_choice = getNumberOnly("Please choose a person type by entering the number:  ")
    
    if int(person_choice) < len(person_types):
        person_class = person_types[int(person_choice)]
        person = person_class(name, age, id_number)
    else:
        print("Invalid choice.")
        return 

    entries[id_number] = person
    ids_list.append(id_number)
    sum_of_ages += age

def searchById():
    id_number = getNumberOnly("Please enter the ID to search for (numbers only): ")
    person = entries.get(id_number)
    if person:
        person.printMyself()
    else:
        print("The record with ID " + id_number + " does not exist in the system.")

def printAgesAverage():
    global sum_of_ages
    if len(entries) == 0:
        print("No entries to calculate the average age.")
    else:
        average_age = sum_of_ages / len(entries)
        print("The average age is: " + str(average_age))

def printAllNames():
    if not entries:
        print("No entries found.")
        return
    for entry in entries.values():
        print(entry.getName())

def printAllIds():
    if not entries:
        print("No entries found.")
        return
    for id_number in entries:
        print(id_number)

def printAllEntries():
    if not entries:
        print("No entries found.")
        return
    for person in entries.values():
        person.printMyself()

def printEntryByIndex():
    if not entries:
        print("No entries found.")
        return
    try:
        index = getNumberOnly("Please enter the index (numbers only): ")
        index_int = int(index)
        id_number = ids_list[index_int]
        entries[id_number].printMyself()
    except TypeError:
        print("Type error... Please make sure the index is a valid number.")
    except IndexError:
        print("Index out of range. Please enter a valid index.")
def wantToLeave():
    while True:
        confirmation = input("Are you sure you want to exit? (y/n): ").lower()
        if confirmation == "y":
            print("Bye bye, have a nice day :)")
            exit()
        elif confirmation == "n":
            return

def saveAllData():
    output_file = input("What is your output file name? ")
    if not output_file.endswith(".csv"):
        output_file += ".csv"

    data_saving = []
    for person in entries.values():
        data_saving.append(person.getInfoDict())

    df = pd.DataFrame(data_saving)
    df.to_csv(output_file, index=False)
    print("Data saved successfully to:", output_file)

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
    while True:
        printMenu()
        choice = input("Please enter your choice (1-9): ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 9:
                raise ValueError
            if choice == MenuOption.SAVE_NEW_ENTRY.value:
                saveNewEntry()
            elif choice == MenuOption.SEARCH_BY_ID.value:
                searchById()
            elif choice == MenuOption.PRINT_AGES_AVERAGE.value:
                printAgesAverage()
            elif choice == MenuOption.PRINT_ALL_NAMES.value:
                printAllNames()
            elif choice == MenuOption.PRINT_ALL_IDS.value:
                printAllIds()
            elif choice == MenuOption.PRINT_ALL_ENTRIES.value:
                printAllEntries()
            elif choice == MenuOption.PRINT_ENTRY_BY_INDEX.value:
                printEntryByIndex()
            elif choice == MenuOption.SAVE_ALL_DATA.value:
                saveAllData()
            elif choice == MenuOption.EXIT.value:
                wantToLeave()
                
        except ValueError:
            print("Invalid input: Please enter a number between 1-9.")       
        input("Press Enter to continue...")

# The start is here!
print("Our software helps you make a list of people's info to keep things organized. (Name, ID, and age)")
try:
    menu()
except KeyboardInterrupt:
    print("\nDont do that please...going out nicely...")
except Exception as e:
    print("Something is wrong. You're not supposed to see this unless there's a problem... :(")
    print("Error details:", str(e))
finally:
    print("Copyrights of this work belongs to: A.P. ©")
