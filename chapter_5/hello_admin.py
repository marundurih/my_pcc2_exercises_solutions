"""
Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they
log in to a website. Loop through the list, and print a greeting to each user.
See page 89 for detail instruction.
"""

usernames = ['ROCK', 'Duende', 'Python', 'g i n', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"--Hello {username}, would you like to see a status report?--")
    else:
        print(f"Hello {username}, thank you for logging in again.")