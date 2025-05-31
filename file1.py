# wrie a python program to read strings and convert all even indexed values into upper case.

value = input("Enter a string:")
string = ''
for i in value:
    pos = value.index(i)
    if pos % 2 == 0:
        upper = i.upper()
        string = string + upper
    else:
        string = string + i
    