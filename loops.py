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

# Loop with continue
while True:
    text = input('Enter text')
    if text == 'exit':
        print('Exiting loop')
        break
    if text == 'break':
        print('To top of the loop')
        continue
print("done !!")
