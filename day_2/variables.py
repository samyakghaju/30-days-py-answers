# Day 2: 30 Days of python programming

# 💻 Exercises - Day 2

# -------------------------------
# Exercises: Level 1
# -------------------------------

# 1. Declare a first name variable and assign a value to it
first_name = 'Samyak'

# 2. Declare a last name variable and assign a value to it
last_name = 'Ghaju'

# 3. Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

# 4. Declare a country variable and assign a value to it
country = 'Nepal'

# 5. Declare a city variable and assign a value to it
city = 'Kathmandu'

# 6. Declare an age variable and assign a value to it
age = 17

# 7. Declare a year variable and assign a value to it
year = 2025

# 8. Declare a variable is_married and assign a value to it
is_married = False

# 9. Declare a variable is_true and assign a value to it
is_true = True

# 10. Declare a variable is_light_on and assign a value to it
is_light_on = True

# 11. Declare multiple variables on one line
name, age, country, is_married = 'Samyak', 17, 'Nepal', False


# -------------------------------
# Exercises: Level 2
# -------------------------------

# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(age))
print(type(is_married))
print(type(name))
print(type(country))

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))

# 3. Compare the length of your first name and your last name
print(len(first_name) == len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# 5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# 6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# 7. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# 8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# 12. The radius of a circle is 30 meters.
radius = 30
pi = 3.14

#     a. Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * radius ** 2

#     b. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * radius

#     c. Take radius as user input and calculate the area.
rad = int(input("Enter radius: "))
area = pi * rad ** 2
circum = 2 * pi * rad

# 13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first = input("Enter your first name: ")
last = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

# 14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# help('keywords')
