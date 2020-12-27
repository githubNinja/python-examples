# Traditional loop
'''
n = 5
while n > 0:
    print('{}{}'.format('This is a while loop and value of the iterator is::', n))
    n = n - 1
print('End of loop')
'''

# Infinite loop
'''
while True:
    text = input('Enter text')
    if text == '#':
        print("Exiting loop due to the # character")
        break
'''

# for loop with numbers
'''for i in [1, 10, 78, 2, 5]:
    print('{}{}'.format("current number is::", i))

# for loop with largest numbers.
i = [9, 41, 12, 3, 74, 15]
maxNumber = max(i)
print("{}{}".format("max number is:", maxNumber))'''


# largest so far by looping.
i = [9, 41, 12, 3, 74, 15]
largestSoFar = 0
for number in i:
    if number > largestSoFar:
        largestSoFar = number
print("{}{}".format("largest so far is::", largestSoFar))


# finding a number with boolean variable
i = [9, 41, 12, 3, 74, 15]
found = False
foundNumber = 0
for number in i:
    if number == 15:
        found = True
        foundNumber = number
        break
print("{}{}".format("Number found and its::", number))


# for loop with Strings.
'''
listOfStrings = ['Joseph', 'Sam', 'Kranty', 'Riddi']
for names in listOfStrings:
    print("{}{}".format("name is::", names))'''





# Loop with continue
'''
while True:
    text = input('Enter text')
    if text == 'exit':
        print('Exiting loop')
        break
    if text == 'break':
        print('To top of the loop')
        continue
print("done !!")'''
