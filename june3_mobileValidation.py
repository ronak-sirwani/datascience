import re

def validMobile(number):
    # ^((\+91)|(0)) :+91 or 0 should be in starting
    # [0-9]{10} : includes only numbers from 0 to 9 with exact length 10
    code= '+91'
    exp= '^((\+91)|(0))\d{10}$'

    return re.match(exp,number)

while True:
    mobile= input("Enter mobile no. : ")
    if validMobile(mobile):
        print("Valid mobile no.")
    else:
        print("Invalid mobile no.")
    resp= input("Want to check more ?? (y/n)")
    if resp=='YES' or resp=='yes' or resp=='y':
        continue
    else:
        break
