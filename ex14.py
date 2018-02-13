from sys import argv

script, user = argv
prompt = '>'

print(f"Hi {user}, I'm the {script} script.")
print("I'd like to ask you a few questions")
print(f"Do you like me {user}?")
likes = input(prompt)

print(f"Where do you live {user}?")
home = input(prompt)

print("What kind of computer do you have?")
pc = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {home}. Not really sure where that is.
And you have a {pc} computer. Very nice!
""")
