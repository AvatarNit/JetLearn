# Task 1
d1 = {"Adam Smith":"A","Judy Paxton":"B+"}
d2 = {"Mary Louis":"A","Patrick White":"C"}

for key,val in d2.items():
    d1[key] = val

for i in d1.items():
    print(i)

# Task 2
A = {"Tamil":92,"English":56,"Maths":88,"Science":97,"Social":89}
B = {"Tamil":78,"English":68,"Maths":88,"Sceince":97,"Social":56}

for key1,val1 in A.items():
    for key2,val2 in B.items():
        if key1 == key2 and val1 == val2:
            print(f"{key1} : {val1} is present in both A and B")


# Task 3
dict1 = {"Name":"Tara","RollNo":130046,"Mark":458,"Age":16}

while True:
    userIn = int(input("1.Change Key\n2. View dict\n3. Exit\n:"))
    if userIn == 1:
        oldKey = input("What key do you want to replace: ")
        newKey = input("What do you want to replace it with: ")
        val = dict1[oldKey]
        del dict1[oldKey]
        dict1[newKey] = val
        print("Changed")
    elif userIn == 2:
        for i in dict1.items():
            print(i)
    elif userIn == 3:
        break
    else:
        print("input a valid option")