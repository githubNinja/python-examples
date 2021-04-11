# is and is not operators
# Use is and is not on None or boolean operators but not floating part numbers , integer numbers
found = False
yes = found is True
print("{}{}".format("is Found is::", yes))

# None keyword is used to define null or an object. None keyword is an object and it's a datatype of class NoneType
# Comparing None with any types like empty string, or 0 always returns False
found = ""
if found is None:
    print("{}{}".format("is Found is::", found))
