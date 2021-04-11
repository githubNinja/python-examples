carsList = ['Mercedes', 'Toyota', 'Audi', 'Ford', 'Chyrsler']
print('car make is:', carsList[0])

# append
carsList.append('Fiat')

# last element from the list.
print('car appended to the list is :', carsList[-1])

# pop
carsList.pop()
print('All cars:', carsList)

# remove
carsList.remove('Mercedes')
print('All cars:', carsList)

# del
del carsList[0]
print('Deleting car and final list:', carsList)

# sorting
carsList.sort()
print('Sorted cars List:', carsList)

names = ['Peter', 'Brad', 'Avery']
names.sort()
print('Sorted names List:', names)
names.reverse()
print('Reverse the List:', names)

# Length of names
print('Length of names List:',len(names))

# iterate over elements of list
for name in names:
    print('names in the list are:', name)



