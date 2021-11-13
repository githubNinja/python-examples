fname = input('Enter file name')
try:
    fHandle = open(fname)
except:
    print('The file can\'t be opened')
    quit()