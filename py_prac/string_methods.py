# String Methods in Python

# group of characters./ group of words => String 

# => A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).


# String methods: -

# 1. len() => to find length of string
# 2. lower() => to convert string to lowercase
# 3. upper() => to convert string to uppercase
# 4. title() => to convert first character of each word to uppercase
# 5. strip() => to remove leading and trailing  extra spceces
# 6. split() => to split a string into a list of substrings
# 7. replace() => to replace a substring with another substring
# 8. capitalize() => to capitalize the first character of a string
# 9. find() => to find the index of a substring within a string (returns -1 if not found)
# 10. count() => to count occurrences of a substring in a string
# 11. index() => to find the index of a substring (raises error if not found)

my_name = "ZIyarat"

my_string = "    hello world "
print("Original String: '", my_string)
print("After using strip(): '", my_string.strip())
print("Length of my_name:", len(my_name))
print("Lowercase my_name:", my_name.lower())
print("Uppercase my_name:", my_name.upper())
print("Title Case my_name:", my_string.title())
my_second_name = "xyz"
print("Capitalized my_string:", my_second_name.capitalize())





