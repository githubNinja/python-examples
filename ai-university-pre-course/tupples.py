tuple_list = ('12', 'opposite', 100, ['blue', 'pink', 'white'], 1, 99)
print("tuple_list:{}".format(tuple_list))

# 2nd Element
print("2nd element:{}".format(tuple_list[2]))

# Change tuple value - THis is not possible as tupples are immutable

#tuple_list[1] = 'Reverse'

# Deleting an element in a tupple is not possible, however deleting complete tupple is possible
print("tuple_list now:{}".format(tuple_list))

#del tuple_list[1] -> Not possible

#Sorting Elements of a tupple
tupple_num = (100,7,88, 12, 91, -1)
print("Sorted tupple_num:{}".format(sorted(tupple_num)))

#This can't be sorted as it contains numbers and strings
         #print("Sorted tupple:{}".format(sorted(tuple_list)))

# Other tupple functions

# count(), index(), sorted()