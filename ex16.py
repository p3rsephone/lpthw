from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you want to cancel, hit CTRL-C (^C).")
print("If you wish to proceed, hit RETURN.")

input("?")

print("Opening the file...")
file = open(filename, 'w')  # Mode is write

print("Erasing the file. Goodbye!")
file.truncate()

print("Now you will write 3 lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Writing the lines...")
file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)

print("Closing the file...")
file.close()

print("Done!")
