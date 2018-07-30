# IO Files

# open file
# you can pass the absolute path as well
my_file = open('myfile.txt')

# read all lines and asign to big_string
big_string = my_file.read()
print(big_string)

# reset cursor
my_file.seek(0)

# returns the lines of the file
lines = my_file.readlines()

# close file
my_file.close()

# with statement - open and close the file
with open('myfile.txt') as my_new_file:
    as_string = my_new_file.read()
    print(as_string)
    my_new_file.seek(0)
    lines = my_new_file.readlines()
    print(lines)

# read file
with open('myfile.txt', mode='r') as my_file:
    as_string = my_file.read()
    print(as_string)

# write in file (depends on permissions)
with open('new_file.txt', mode='w') as my_file:
    my_file.write('there is just a line\n')

# append to on file
with open('myfile.txt', mode='a') as my_file:
    my_file.write('this is a brand new line\n')

# read and write (depends on permissions)
# with open('myfile.txt', mode='r+') as my_file:
    # as_string = my_file.read()

# write and read (depends on permissions)
# with open('myfile.txt', mode='w+') as my_file:
    # as_string = my_file.read()
