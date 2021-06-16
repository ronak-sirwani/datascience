import random

def passwordGenerator(passw):
    numbers= [str(i) for i in range(10)]
    capital_alphabets= [chr(i) for i in range(65,91)]
    small_alphabets= [chr(i) for i in range(97,123)]
    special_char= ['!','@','#','$','%','^','&','*']


    freq_numbers= int(0.3*passw)
    freq_capalpha= int(0.2*passw)
    freq_smallalpha= int(0.2*passw)
    freq_special= int(0.3*passw)
    total= freq_numbers+freq_capalpha+freq_smallalpha+freq_special 
    if total < passw:
        freq_numbers+= passw-total

    passw_num= random.choices(numbers,k=freq_numbers)
    passw_calpha= random.choices(capital_alphabets,k=freq_capalpha)
    passw_salpha= random.choices(small_alphabets,k=freq_smallalpha)
    passw_sp= random.choices(special_char,k=freq_special)

    temp= passw_num+passw_calpha+passw_salpha+passw_sp

    new_passw= random.choices(temp,k=passw)

    return "".join(new_passw)


length= int(input("Enter the length of password : "))
print("New password generated is : {}".format(passwordGenerator(length)))