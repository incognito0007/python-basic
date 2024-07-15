# def fact(n):
#     if n == 0:
#         return 1
#     ans = n * fact(n-1)
#     return ans
#
# print(fact(6))

# def printNtoOne(n):
#     if n == 0:
#         return
#     print(n)
#     printNtoOne(n-1)
#
# printNtoOne(5)

# def printSumOneToN(n):
#     if n == 1:
#         return 1
#     sum = n + printSumOneToN(n-1)
#     return sum
#
# print(printSumOneToN(10))

# def raiseToPower(a, b):
#     if b == 0:
#         return 1
#     ans = a * raiseToPower(a, b-1)
#     return ans
#
# print(raiseToPower(4, 3))

# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for i in range(1, 8):
#     print(fibonacci(i))