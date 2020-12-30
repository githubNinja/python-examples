fileHandle = open('files/text.file')

# To iterate thru the sequence of lines in the file use a for statement.
# The print statement adds  a new line to each line to remove the extra space use rstrip()
# new line is considered as extra white space and is stripped.

for line in fileHandle:
    print('{}{}'.format('file contents are::', line.rstrip()))


# Reading the whole file using the length of the file
fileHandle = open('files/text.file')
readLine = fileHandle.read()
print('length of the file:{}'.format(len(readLine)))
print('{}{}'.format('readLine::', readLine[:71]))
