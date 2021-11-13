
# Count the number of lines in a file and printing lines.

fd = open('../../files/text.file', 'r')
count = 0
for line in fd:
    count = count +1
    print('{}{}'.format('line from file is::', line))
print('{}{}'.format('no of lines::', count))