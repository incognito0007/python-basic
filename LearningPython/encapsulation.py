# bundles the attributes together in one entity that is class

# Exception handling in OOPS
# try except final

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    result = a / b
except:
    result = None
    print("Error : cannot be divided by zero")
finally:
    print("Division operation completed", result)
