import re

def validEmail(email):
    # [\w-]{1,20} : includes alphanumeric and some special characters like -,_ with length 1 to 20
    # @ : includes @
    # \w{2,20} : includes alphanumeric and some special characters like _ with length 2 to 20
    # \. : include .
    # \w{2,3}: includes domain name with length 2 or 3

    exp= "^[\w-]{1,20}[\.]*[\w-]{1,20}@\w{2,20}\.\w{2,3}"
    return re.match(exp,email)

while True:
    email= input("Enter email: ")
    if validEmail(email):
        print("Valid email")
    else:
        print("Invalid email")
    resp= input("Want to check more ?? (y/n)")
    if resp=='YES' or resp=='yes' or resp=='y':
        continue
    else:
        break
