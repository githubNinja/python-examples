# for item in

largest = 0
i = [1, 2, 3, 1009, 876, 2456, 652]
for number in i:
    if number > largest:
        largest = number
print("{}{}".format("The largest number is ::", largest))

# Ranges
for i in range(1, 200):
    print("{}{}".format("i is::", i))

# Ranges diff version
for i in range(50):
    print("{}{}".format("i is::", i))

# List with ranges
myList = range(10)
print("{}{}".format("list is::", list(myList)))

# The 3rd parameter is step
myList = range(1, 30, 1)
print("{}{}".format("list is::", list(myList)))

dictionary = {'key1': 'value1', 'key2': ' value2', 'key3': '3', 'key4': 5}
dictionary.update({'key4', 78})
print(f'dictionary::{dictionary}')
print(f" dict value::{dictionary['key3']} and {dictionary['key4']}")


