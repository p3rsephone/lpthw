# F-Strings and Formatting 2.0

typesOfPeople = 10
x = f"There are {typesOfPeople} types of people."  # this is an f-string

binary = "binary"
doNot = "don't"
y = f"Those who know {binary} and those who {doNot}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
# The {} is a space left for formatting
jokeEval = "Isn't that joke so funny?! {}"

# In here we specify what is in the format.
print(jokeEval.format(hilarious))
# Other ways to do the same thing
#
# print(jokeEval.format("True"))
# print("Isn't that joke so funny?! {}".format("True"))

left = "This is the left side of..."
right = "a string with a right side."

# Adding strings
print(left + right)

# Multiplying Strings
print("." * 100)  # ..........

# Formatting 2.0
formatter = "{} {} {} {}"
# Which is actually the same as print(xxx,xxx,xxx,xxx)

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# The next one says turn the string formatter and use it as a thing
print(formatter.format(formatter, formatter, formatter, formatter))
print(
    formatter.format("Roses are red", "Violets are blue", "I hate rhyming",
                     "Vaccum, Noodles, Hobo"))
# This last one should've been like this
print(
    "Roses are red",
    "Violets are blue",
    "I hate rhyming",
    "Vaccum, Noodles, Hobo",
    sep='\n')
