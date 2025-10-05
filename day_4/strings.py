# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Answer:
concatenated_string = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(concatenated_string)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Answer:
concatenated_string_2 = ' '.join(['Coding', 'For', 'All'])
print(concatenated_string_2)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
# Answer:
company = "Coding For All"

# 4. Print the variable company using print().
# Answer:
print(company)

# 5. Print the length of the company string using len() method and print().
# Answer:
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
# Answer:
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
# Answer:
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Answer:
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
# Answer:
first_word = company.split()[0]
print(first_word)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Answer:
contains_coding = 'Coding' in company
print(contains_coding)

# 11. Replace the word coding in the string 'Coding For All' to Python.
# Answer:
replaced_string = company.replace('Coding', 'Python')
print(replaced_string)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
# Answer:
string_to_change = 'Python for Everyone'
changed_string = string_to_change.replace('Everyone', 'All')
print(changed_string)

# 13. Split the string 'Coding For All' using space as the separator (split()) .
# Answer:
split_string = company.split(' ')
print(split_string)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# Answer:
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = tech_companies.split(', ')
print(split_companies)

# 15. What is the character at index 0 in the string Coding For All.
# Answer:
char_at_index_0 = company[0]
print(char_at_index_0)

# 16. What is the last index of the string Coding For All.
# Answer:
last_index = len(company) - 1
print(last_index)

# 17. What character is at index 10 in "Coding For All" string.
# Answer:
char_at_index_10 = company[10]
print(char_at_index_10)

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Answer:
phrase = 'Python For Everyone'
acronym = ''.join([word[0] for word in phrase.split()])
print(acronym)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
# Answer:
phrase_2 = 'Coding For All'
acronym_2 = ''.join([word[0] for word in phrase_2.split()])
print(acronym_2)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# Answer:
phrase_3 = 'Coding For All'
index_of_C = phrase_3.index('C')
print(index_of_C)

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# Answer:
index_of_F = phrase_3.index('F')
print(index_of_F)

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Answer:
phrase_4 = 'Coding For All People'
last_index_of_l = phrase_4.rfind('l')
print(last_index_of_l)

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Answer:
phrase_5 = 'You cannot end a sentence with because because because is a conjunction'
first_index_of_because = phrase_5.index('because')
print(first_index_of_because)

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Answer:
last_index_of_because = phrase_5.rindex('because')
print(last_index_of_because)

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Answer:
start = phrase_5.index('because')
end = start + len('because because because')
sliced_phrase = phrase_5[start:end]
print(sliced_phrase)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Answer:
first_occurrence_because = phrase_5.find('because')
print(first_occurrence_because)

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Answer:
sliced_phrase_2 = phrase_5[start:end]
print(sliced_phrase_2)

# 28. Does 'Coding For All' start with a substring Coding?
# Answer:
starts_with_coding = company.startswith('Coding')
print(starts_with_coding)

# 29. Does 'Coding For All' end with a substring coding?
# Answer:
ends_with_coding = company.endswith('coding')
print(ends_with_coding)

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Answer:
string_with_spaces = '   Coding For All      '
trimmed_string = string_with_spaces.strip()
print(trimmed_string)

# 31. Which one of the following variables return True when we use the method isidentifier():
#     30DaysOfPython
#     thirty_days_of_python
# Answer:
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
isidentifier_var1 = var1.isidentifier()
isidentifier_var2 = var2.isidentifier()
print(isidentifier_var1)  # False
print(isidentifier_var2)  # True

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Answer:
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)

# 33. Use the new line escape sequence to separate the following sentences.
#     I am enjoying this challenge.
#     I just wonder what is next.
# Answer:
sentences = "I am enjoying this challenge.\nI just wonder what is next."
print(sentences)

# 34. Use a tab escape sequence to write the following lines.
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
# Answer:
lines = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(lines)

# 35. Use the string formatting method to display the following:
#     radius = 10
#     area = 3.14 * radius ** 2
#     The area of a circle with radius 10 is 314 meters square.
# Answer:
radius = 10
area = 3.14 * radius ** 2
formatted_string = f'The area of a circle with radius {radius} is {area} meters square.'
print(formatted_string)

# 36. Make the following using string formatting methods:
#     8 + 6 = 14
#     8 - 6 = 2
#     8 * 6 = 48
#     8 / 6 = 1.33
#     8 % 6 = 2
#     8 // 6 = 1
#     8 ** 6 = 262144
# Answer:
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')