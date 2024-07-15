# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     # print(i)
#     sum += i
# print(sum)

# def sum(n):
#     res = 0
#     for i in range(1, n+1):
#         res += i
#     return res
#
# print(sum(10))

# def printHello():
#     print("Hello")
#
# printHello()


# pass by value

def addone(x):
    x = x + 1
    print("inside function value of x is:", x)

x = 5
addone(x)
print("outside function value of x is:", x)


# pass by reference

def modifyList(lst):
    lst.append(4)
    print("inside function", lst)

lst = [1, 2, 3]
modifyList(lst)
print("outside function", lst)

# def factorial(n):
#     res = 1
#     # while n != 1:
#     #     res = res * n
#     #     n = n-1
#
#     for i in range(1, n+1):
#         res *= i
#     return res
#
# inputInt = int(input("enter a number:"))
# ans = factorial(inputInt)
# print(f"factorial of {inputInt} is {ans}")