# def is_odd():
#     value = int(input("Enter a numeric value"))
#     if value % 2 == 1:
#         print("it's an odd number")
#     else:
#         print("Its an even number")


# def is_odd(value):
#     if value % 2 == 1:
#         print("Its an odd number")
#         return "True"
        

# value = int(input("Enter an integer value"))
# value1 = int(input("Enter one more interger"))
# is_odd(value)

def is_odd(value, value1):
    if value > value1:
        return str("First Value is higher")
    else:
        return str("Second is higher")


value = int(input("Enter a Value  "))
value1 = int(input("Enter second value  "))
is_true = is_odd(value, value1)
print(is_true)