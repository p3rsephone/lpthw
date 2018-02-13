from sys import argv

script, filename = argv

print("************************ WELCOME ************************")
print("This is cat in python.")
print(f"I will now read {filename}.\n")

file = open(filename)  # Open default is READ TEXT
print(file.read())
