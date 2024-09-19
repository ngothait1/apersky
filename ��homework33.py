def insert_20(name_id_20):
    print("Please enter name + ID 20 times")
    for i in range(20):
        name = input("Insert name: ")
        id_number = int(input("Insert ID number: "))
        name_id_20[name] = id_number


def insertNameAndDicGetIndex(name_id_20):
     name_to_search = input("Enter the name to search get his index, if he not exist you will get -1: ")
     for index, key in enumerate(name_id_20):
         if key == name_to_search:
            print("The index of " + name_to_search + " is: " + str(index))
            return index
     else: print("-1")


def dicNameIdAge(name_id_age):
    print("Please enter name, ID, and age 3 times to create another dictionary") 
    for i in range(3):
        name = input("Insert name: ")
        id_number = int(input("Insert ID number: "))
        age = int(input("Insert age: "))
        name_id_age[name] = {"ID": id_number, "Age": age}    
      
name_id_20 = {}
name_id_age = {}
# 1
insert_20(name_id_20)
# 2
insertNameAndDicGetIndex(name_id_20)
# 3
print(name_id_20)
# 4
dicNameIdAge(name_id_age)
