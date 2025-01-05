# n1 = int(input("enter length of list1: "))
# list1 = list()
# for i in range(n1):
#     list1.append(int(input(f"element {i+1}:")))

# n2 = int(input("enter length of list2: "))
# list2 = list()
# for i in range(n2):
#     list2.append(int(input(f"element {i+1}:")))

list1 = [1, 1, 2]
list2 = [2, 3, 4]
diff = [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]
print(diff)