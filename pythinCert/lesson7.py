# # Task 1
# gList = []

# while True:
#     userIn = int(input("1. Add Item\n2. Remove Item\n3. View List\n4. To Exit\n:"))
#     if userIn == 1:
#         newItem = input("What would you like to add: ")
#         gList.append(newItem)
#         print(f"Added {gList[len(gList)-1]}")
#     elif userIn == 2:
#         removeItem = input("What would you like to remove: ")
#         gList.remove(removeItem)
#         print("Item removed")
#     elif userIn == 3:
#         print("Grocery List")
#         for i in range(len(gList)):
#             print(f"{i+1}. {gList[i]}")
#     elif userIn == 4:
#         break
#     else:
#         print("please select a valid option")

# # Task 2
# gradesList = input("Input your grades seperated by commas: ").split(",")
# avg = 0
# for i in gradesList:
#     avg += int(i)
# avg = avg/len(gradesList)
# if avg > 99.5:
#     print("A+")
# elif avg > 92.5:
#     print("A")
# elif avg > 89.5:
#     print("A-")
# elif avg > 86.5:
#     print("B+")
# elif avg > 82.5:
#     print("B")
# elif avg > 79.5:
#     print("B-")
# elif avg > 76.5:
#     print("C+")
# elif avg > 72.5:
#     print("C")
# elif avg > 69.5:
#     print("C-")
# elif avg > 66.5:
#     print("D+")
# elif avg > 62.5:
#     print("D")
# elif avg > 59.5:
#     print("D-")
# else:
#     print("F")

# Task 3
taskList = []

while True:
    userIn = int(input("1. Add Item\n2. Remove Item\n3. View List\n4. To Exit\n:"))
    if userIn == 1:
        newItem = input("What would you like to add: ")
        newItemP = int(input("What is the priority: "))
        taskList.append([newItem,newItemP])
        print(f"Added {taskList[len(taskList)-1]}")
    elif userIn == 2:
        removeItem = input("What would you like to remove: ")
        for i in taskList:
            if i[0] == removeItem:
                taskList.remove(i)
                break
        print("Item removed")
    elif userIn == 3:
        print("Task List")
        tempList = taskList.copy()
        while len(tempList) != 0:
            topPrior = 0
            topIndex = 0
            for i in range(len(tempList)):
                if tempList[i][1] > topPrior:
                    topPrior = tempList[i][1]
                    topIndex = i
            print(f"Task: {tempList[topIndex][0]} Priority: {tempList[topIndex][1]}")
            tempList.pop(topIndex)
    elif userIn == 4:
        break
    else:
        print("please select a valid option")
