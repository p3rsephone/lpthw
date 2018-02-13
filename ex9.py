# Printing habits

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With three double quotes.
It's like markdown (the code formatting)
We can type as much as we want
Just line after line!
""")

# Tabs!
intro = "*********************************************"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."  # escape the (back)slash

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Delete lists
"""

print(intro, tabby_cat, persian_cat, backslash_cat, fat_cat, sep="\n\n")
