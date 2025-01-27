# Task 1
contactList = []

while True:
    userIn = int(input("1. Add Contact\n2. Remove Contact\n3. View Contacts\n4. To Exit\n:"))
    if userIn == 1:
        newName = input("Name: ")
        newPhone = input("Phone: ")
        contactList.append((newName,newPhone))
        print(f"Added {contactList[len(contactList)-1]}")
    elif userIn == 2:
        removeItem = input("Who would you like to remove: ")
        for i in contactList:
            if i[0] == removeItem:
                contactList.remove(i)
                break
        print("Item removed")
    elif userIn == 3:
        print("Contact List")
        for i in contactList:
            print(i)
    elif userIn == 4:
        break
    else:
        print("please select a valid option")

# Task 2

employeeList = []

while True:
    userIn = int(input("1. Add Employee\n2. Remove Employee\n3. View Employees\n4. To Exit\n:"))
    if userIn == 1:
        newName = input("Name: ")
        newID = input("ID: ")
        newDepart = input("Department: ")
        employeeList.append((newName,newID,newDepart))
        print(f"Added {employeeList[len(employeeList)-1]}")
    elif userIn == 2:
        removeItem = input("Who would you like to remove: ")
        for i in employeeList:
            if i[0] == removeItem:
                employeeList.remove(i)
                break
        print("Item removed")
    elif userIn == 3:
        print("Employee List")
        for i in employeeList:
            print(i)
    elif userIn == 4:
        break
    else:
        print("please select a valid option")

# # Task 3

flightList = []

while True:
    userIn = int(input("1. Add Flight\n2. Remove Flight\n3. View Flights\n4. Find Flight\n5. To Exit\n:"))
    if userIn == 1:
        newFrom = input("From: ")
        newTo = input("To: ")
        newID = input("ID: ")
        flightList.append((newFrom,newTo,newID))
        print(f"Added {flightList[len(flightList)-1]}")
    elif userIn == 2:
        removeItem = input("What flight would you like to remove(ID): ")
        for i in flightList:
            if i[2] == removeItem:
                flightList.remove(i)
                break
        print("Flight removed")
    elif userIn == 3:
        print("Flight List")
        for i in flightList:
            print(i)
    elif userIn == 4:
        flight = input("Where do you want to go?\n: ")
        print(f"Flights to {flight}")
        for i in flightList:
            if i[1] == flight:
                print(i)
    elif userIn == 5:
        break
    else:
        print("please select a valid option")
