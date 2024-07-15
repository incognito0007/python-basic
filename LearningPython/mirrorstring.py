inputString = input("enter a string: ")
n = int(input("enter n:"))

alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse = alphabets[::-1]

dict1 = dict(zip(alphabets, reverse))

prefix = inputString[0:n-1]
funStr = inputString[n-1:]

mirror = ""

for i in range(0, len(funStr)):
    mirror = mirror + dict1[funStr[i]]

res = prefix + mirror
print(res)
