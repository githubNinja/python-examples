integers = []
i = 0
count = 0
while i < 5:
    integer = input("enter an integer between 1 and 50: ")
    integer_user = int(integer)
    if count == 5:
        break
    if 20 < integer_user <= 50:
        integers.append(integer_user)
    count = count + 1

print("integers are::", integers)
'''
else:
    print("Thanks for Entering 5 integers!")
    print("integers are::", integers)'''


a = 10
b = 2.3
c = a*b
print(type(c))