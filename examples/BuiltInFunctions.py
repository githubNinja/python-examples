# max function, min function , float(), type() and int()

x = max(100, 200)
print('{}{}'.format('Max value is ', x))
# Min function
minValue = min(100, 200)
print('{}{}'.format('Min value is::', minValue))

print('{}{}'.format('float value is::', float(x)))
floatValue = float(x) / 12.5
print('{}{}'.format('float value is::', floatValue))

floatTypeOf = type(floatValue)
intTypeOf = type(minValue)

print('{} {} {}'.format('type of class is::', floatTypeOf, intTypeOf))

# String format of Integer..
i = int('457')
print('{}'.format('hello in integer:'), i + 2)


