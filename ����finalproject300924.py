def saveNewEntry():
    global sum_of_ages, count_of_entries  # Allow global variables edit.
    print("You selected Option 1 - Save a new entry")
    name = input("Please enter a name: ")
    # Check if ID is ok.
    while True:
        id_number = input("Please enter the ID of the name (numbers only): ")
        if id_number.isdigit():
            if id_number in entries:
                print("ID " + id_number + " already exists.")
                return  
            else:
                break  
        else:
            print("Invalid ID. Please enter numbers only.")
    # Check if age is ok.
    while True:
        age = input("Please enter the age: ")
        if age.isdigit():
            age = int(age) 
            break
        else:
            print("Invalid age. Please enter a valid number.")
    # Save the new entry dic in another dic
    entries[id_number] = {'name': name, 'age': age}
    # Update sum of ages and count of entries
    sum_of_ages += age
    count_of_entries += 1
    menu()

def searchById():
    print("You selected Option 2 - Search by ID")
    id_number = input("Please enter the ID to search for (numbers only): ")
    if id_number.isdigit():
        if id_number in entries:
            print("ID: " + id_number)
            print("Name: " + entries[id_number]['name'])
            print("Age: " + str(entries[id_number]['age']))
        else:
            print("The record with ID " + id_number + " does not exist in the system.")
    else:
        print("Invalid ID. Please enter numbers only.")
    menu()

def printAgesAverge():
    print("You selected Option 3 - Print ages average")
    if count_of_entries == 0:
        print("No entries to calculate the average age.")
    else:
        average_age = sum_of_ages / count_of_entries
        print("The average age is: " + str(average_age))
    menu()

def printAllNames():
    print("You selected Option 4 - Print all names")
    if not checkIfEntriesExist():
        return
    for entry in entries.values():
        print(entry['name'])
    menu()

def printAllIds():
    print("You selected Option 5 - Print all IDs")
    if not checkIfEntriesExist():
        return
    for id_number in entries:
        print(id_number)
    menu()

def printAllEntries():
    print("You selected Option 6 - Print all entries")
    if not checkIfEntriesExist():
        return
    for id_number, entry in entries.items():
        print("ID: " + id_number + ", Name: " + entry['name'] + ", Age: " + str(entry['age']))
    menu()

def printEntryByIndex():
    print("You selected Option 7 - Print entry by index")
    if not checkIfEntriesExist():
        return
    index_input = input("Please enter the index (numbers only): ")
    if not index_input.isdigit():
        print("Invalid input.")
    else:
        index = int(index_input)
        if index < 0 or index >= len(entries):
            print("Index out of range. Maximum allowed index is: " + str(len(entries) - 1))
        else:
            id_number = list(entries.keys())[index]
            entry = entries[id_number]
            print("ID: " + id_number + ", Name: " + entry['name'] + ", Age: " + str(entry['age']))
    menu()

def wantToLeave():
    while True:
        confirmation = input("Are you sure you want to exit? (y/n): ").lower()
        if confirmation == 'y':
            print("Bye bye, have a nice day :)")
            exit()  
        elif confirmation == 'n':
            menu()

# function to check if there are any entries at all
def checkIfEntriesExist():
    if len(entries) == 0:
        print("No entries found.")
        menu()
        return False
    return True

def menu():
    print("Please choose an option:")
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")
    
    choice_input = input("Please enter your choice (1-8): ")

    if choice_input.isdigit():
        choice = int(choice_input)
        
        if choice in range(1, 9):
            if choice == 1:
                saveNewEntry()
            elif choice == 2:
                searchById()
            elif choice == 3:
                printAgesAverge()
            elif choice == 4:
                printAllNames()
            elif choice == 5:
                printAllIds()
            elif choice == 6:
                printAllEntries()
            elif choice == 7:
                printEntryByIndex()
            elif choice == 8:
                wantToLeave()
        else:
            print("Invalid choice. Please choose a number between 1 and 8.")
            menu()
    else:
        print("Invalid input. Please enter a valid number.")
        menu()

sum_of_ages = 0
count_of_entries = 0
entries = {}
# The start is here!
print("Our software helps you make a list of people's info to keep things organized.(Name, ID and age)")
menu()