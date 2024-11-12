import pandas as pd
import os
from person import Person
from student import Student
from employee import Employee
from utils import getNumberOnly
from menuoption import MenuOption

SUM_OF_AGES = 0
ENTRIES = {}
IDS_LIST = []

def saveNewEntry():
    global SUM_OF_AGES, ENTRIES, IDS_LIST
    name = input("Please enter a name: ")
    id_number = getNumberOnly("Please enter the ID of the name (numbers only): ")

    if id_number in ENTRIES:
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

    ENTRIES[id_number] = person
    IDS_LIST.append(id_number)
    SUM_OF_AGES += age

def searchById():
    id_number = getNumberOnly("Please enter the ID to search for (numbers only): ")
    person = ENTRIES.get(id_number)
    if person:
        person.printMyself()
    else:
        print("The record with ID " + id_number + " does not exist in the system.")

def printAgesAverage():
    global SUM_OF_AGES
    if len(ENTRIES) == 0:
        print("No entries to calculate the average age.")
    else:
        average_age = SUM_OF_AGES / len(ENTRIES)
        print("The average age is: " + str(average_age))

def printAllNames():
    if not ENTRIES:
        print("No entries found.")
        return
    for entry in ENTRIES.values():
        print(entry.getName())

def printAllIds():
    if not ENTRIES:
        print("No entries found.")
        return
    for id_number in ENTRIES:
        print(id_number)

def printAllEntries():
    if not ENTRIES:
        print("No entries found.")
        return
    for person in ENTRIES.values():
        person.printMyself()

def printEntryByIndex():
    if not ENTRIES:
        print("No entries found.")
        return
    try:
        index = getNumberOnly("Please enter the index (numbers only): ")
        index_int = int(index)
        id_number = IDS_LIST[index_int]
        ENTRIES[id_number].printMyself()
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
    for person in ENTRIES.values():
        data_saving.append(person.getInfoDict())

    df = pd.DataFrame(data_saving)
    df.to_csv(output_file, index=False)
    print("Data saved successfully to:", output_file)

def printMenu():
    print("Please choose an option:")
    for option in MenuOption:
        print(str(option.value) + ". " + option.name)

def menu():
    while True:
        printMenu()
        choice = input("Please enter your choice (1-9): ")
        if choice and 1 <= int(choice) <= len(MenuOption):
            choice = MenuOption(int(choice))
            
            if choice == MenuOption.SAVE_NEW_ENTRY:
                saveNewEntry()
            elif choice == MenuOption.SEARCH_BY_ID:
                searchById()
            elif choice == MenuOption.PRINT_AGES_AVERAGE:
                printAgesAverage()
            elif choice == MenuOption.PRINT_ALL_NAMES:
                printAllNames()
            elif choice == MenuOption.PRINT_ALL_IDS:
                printAllIds()
            elif choice == MenuOption.PRINT_ALL_ENTRIES:
                printAllEntries()
            elif choice == MenuOption.PRINT_ENTRY_BY_INDEX:
                printEntryByIndex()
            elif choice == MenuOption.SAVE_ALL_DATA:
                saveAllData()
            elif choice == MenuOption.EXIT:
                wantToLeave()
        else:
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