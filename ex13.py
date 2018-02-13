# Command Line Argument
from sys import argv
# This is me dividing the argv into components that matter - aka think Matlab
# Also called unpacking
script, first, second, third = argv
# Also, if the number of args isn't the one py is expecting an error occurs

print("The script name is", script)
print("The first arg is", first)
print("The second arg is", second)
print("The third arg is", third)
