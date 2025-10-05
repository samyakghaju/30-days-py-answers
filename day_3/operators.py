# -------------------------------
# Day 3: Python - Operators
# -------------------------------

# Declare your age as an integer variable
age = 25

# Declare your height as a float variable
height = 5.9

# Declare a variable that stores a complex number
complex_num = 3 + 4j

# -------------------------------
# Calculate the area of a triangle
# Formula: area = 0.5 * base * height
# -------------------------------
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is", area)

# -------------------------------
# Calculate the perimeter of a triangle
# Formula: perimeter = a + b + c
# -------------------------------
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

# -------------------------------
# Calculate area and perimeter of a rectangle
# Area = length * width
# Perimeter = 2 * (length + width)
# -------------------------------
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is", area)
print("The perimeter of the rectangle is", perimeter)

# -------------------------------
# Calculate area and circumference of a circle
# Area = π * r^2
# Circumference = 2 * π * r
# -------------------------------
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print("The area of the circle is", area)
print("The circumference of the circle is", circumference)

# -------------------------------
# Calculate slope, x-intercept, and y-intercept of y = 2x - 2
# -------------------------------
slope = 2
x_intercept = 2 / 2  # y = 0 → 0 = 2x - 2 → x = 1
y_intercept = -2     # x = 0 → y = -2
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# -------------------------------
# Calculate slope and Euclidean distance between (2,2) and (6,10)
# -------------------------------
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Slope:", m)
print("Euclidean distance:", d)

# Compare slopes
print("Slopes are equal:", slope == m)

# -------------------------------
# Calculate y = x² + 6x + 9 and find when y = 0
# -------------------------------
for x in range(-10, 11):
    y = x ** 2 + 6 * x + 9
    print(f"When x = {x}, y = {y}")
    if y == 0:
        print("👉 y is zero when x =", x)

# -------------------------------
# String operations
# -------------------------------
print("Length of 'python':", len('python'))
print("Length of 'dragon':", len('dragon'))
print("Are lengths equal?", len('python') == len('dragon'))

# Check if 'on' is found in both words
print("'on' in both 'python' and 'dragon':", 'on' in 'python' and 'on' in 'dragon')

# Check if 'jargon' is in a sentence
print("'jargon' in the sentence:", 'jargon' in "I hope this course is not full of jargon.")

# Check that 'on' is not in both
print("'on' not in both 'dragon' and 'python':", 'on' not in 'dragon' and 'on' not in 'python')

# -------------------------------
# Type conversion examples
# -------------------------------
length_python = len('python')
length_float = float(length_python)
length_str = str(length_float)
print("Length of 'python' as float:", length_float)
print("Length of 'python' as string:", length_str)

# -------------------------------
# Check if a number is even or odd
# -------------------------------
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# -------------------------------
# Comparison operations
# -------------------------------
print("7 // 3 == int(2.7):", 7 // 3 == int(2.7))
print("Type of '10' == type of 10:", type('10') == type(10))
print("int(float('9.8')) == 10:", int(float('9.8')) == 10)

# -------------------------------
# Calculate weekly earning
# -------------------------------
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is", pay)

# -------------------------------
# Calculate number of seconds lived
# -------------------------------
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# -------------------------------
# Display table
# -------------------------------
"""
This program displays the following table:

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
