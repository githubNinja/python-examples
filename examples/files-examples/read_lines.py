fp = open('../../files/text.file', 'r')
lines = fp.readlines()
for line in lines:
    print('{}{}'.format('lines are::', line.strip()))
fp.close()

# Get 5 characters from a line
fp = open('../../files/text.file', 'r')
line = fp.readline()
typeis = type(line)

print('{}{}'.format('stripped line:', line[:5]))

# Get only 2 lines in the file.
fp = open('../../files/text.file', 'r')
line = fp.readlines()
for each_line in line[:2]:
    print('{}{}'.format('print each line:', each_line))

fp.close()

#
fp = open('../../files/text.file', 'r')
#line = fp.readline(2)
#print('same line:', line)
#same line: Welcome to python and this is the second
print('same line:', fp.read(2))
#print('file chars length:', len(line))
