
try:
    date = eval(input("Please enter a date: "))
except SyntaxError:
    print("Invalid date entered ")
else:
    print("You have entered: ", date)


# example of the IOError
try:
    name = input("Enter the filename you want to open :")
    f = open(name, 'r')
except IOError:
    print("File not found :", name)
else:
    n = len(f.readlines())
    print(name, " has ", n, " lines.")
    f.close()

