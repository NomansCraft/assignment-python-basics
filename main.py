# Variables and data types
print("Variable and data type:")

name = "Md. Ohiduzzaman"
print(type(name))
age = 38
print(type(age))
is_student = False
print(type(is_student))

# Arithmetic operators
print("Arithmetic operators:")
addition = age + 10
subtraction = age - 10
multiplication = age * 2
division = age / 2
 
print(f"Addition = {addition}\nSubtraction = {subtraction}\nMultiplication ={multiplication}\nDivision = {division}")

# Comparison operators
print()
print("Comparison operators:")
base_age = 18
is_greater_than = base_age < age
is_less_than = base_age > age
is_same_age = base_age == age

print(f"Age is greater than 18? Answer: {is_greater_than}")
print(f"Age is leas than 18? Answer: {is_less_than}")
print(f"Age is 18? Answer: {is_same_age}")

# Logical operators
print()
print("Logical operators:")
is_interested_peogramming = True
print(is_interested_peogramming or is_less_than)
print(is_interested_peogramming and is_greater_than)

# Assignment operators
print()
print("Assignment operators")
num = 50
print(num)
num += 10
print(num)
num -= 20
print(num)
num *= 2
print(num)
num /= 10
print(num)

# Identity operator
print()
print("Identity operator:")
num1 = 50
num2 = 60
print(num1 is num2)
print(num1 is not num2)

# Membership operators: 
print()
print("Membership operators: ")
my_arr = [1, 2, 3, 4, 5]
print(5 in my_arr)
print(7 not in my_arr)




