# length of the string.
name = 'Peter'
print("{}{}".format("Length of the String::", (len(name))))

# Slicing Strings
name = 'Welcome to Python'
# start at index 0 and end before index 4. which is exclusive
print(name[0:4])

# start at index 8 and till end of the String
print(name[8:])

# Prints entire string
print(name[:])

# Logical operator - The in keyword to check if one String is "in" another string
name = 'Welcome'
if 'come' in name:
    print('come exists in name')

# == to compare strings
word = 'Hi'
if word == 'hello' or word == 'hi':
    print('This is a hello or hi')

    if word < 'hello':
        print('word is < hello')
    else:
        print('word is > hello')

# lower case, upper case
print("{}{}".format("lower case ::", word.lower()))
print("{}{}".format("lower case ::", word.upper()))

# find
fruit = "apple"
fruit.find('ap')

# replace() is like a search and replace operation in a word.
name = " Hello Krantz "
modifiedName = name.replace('Hello', 'Welcome')
print("{}{}".format("name is::", modifiedName))


# lstrip() and rstrip() removes the left or right whitespace
# strip() removes both beggining and ending whitespace

# Prefixes
line = "Have a great day !!"
if line.startswith('Have'):
    print(' line starts with Have')
