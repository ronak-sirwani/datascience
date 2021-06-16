def classify(val):
    if val >= -5 and val < -2.7:
        return 1
    if val >=-2.7 and val < -0.4:
        return 2
    if val >= -0.4 and val < 2:
        return 3
    if val >= 2 and val < 3.5:
        return 4
    if val >=3.5 and val <=5:
        return 5
          
while True:
    score= float(input("Enter score (between -5 to 5): "))
    print("Rating is : {}".format(classify(score)))
    
    resp= input("Want to enter more score: ")
    if resp=='y' or resp=='yes':
        continue
    else:
        break