fruits = ["Apple", "Orange", "Guava", "Banana", "Mango"]
# print(type(fruits))
# print(len(fruits))
# print(len(fruits[3]))
#
# print("if banana is in the list or not : ", "Banana" in fruits)

# print(fruits[1:4])
# print(fruits[-5 : -1])
# for fruit in fruits:
#     print(fruit)

# fruits.append("Papaya")
# fruits.insert(4, "Peach")
#
# print(fruits)

# marks = [98, 99, 97, 92, 91]
#
# fruits.extend(marks)
#
# print(fruits)
#
# fruits.remove(98)
# print(fruits)

# fruits.pop()
# print(fruits)
#
# fruits.pop(3)
# print(fruits)

# fruits.sort()
# fruits.sort(reverse=True)
# print(fruits)

# ------------------------------ LIST COMPREHENSION -------------------

# num = [30, 23, 27, 18, 33, 15, 26]
# new_num = [i for i in num if i >= 25];    #This is list comprehension
#
# new_num = []
# for i in num:
#     if i >= 25:
#         new_num.append(i)
# print(new_num)


# ------------------ Copying A LIST ---------------------

# num = [30, 23, 27, 18, 33, 15, 26]
# new_num = num.copy()
# print(new_num)


inp_list = [23, 65, 19, 90]
temp = inp_list[0]
inp_list[0] = inp_list[2]
inp_list[2] = temp

print(inp_list)
