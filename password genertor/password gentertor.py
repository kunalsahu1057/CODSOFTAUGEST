import random
import string
print("!! PASSWORD GENERATOR !!")
print("Please do not share your password with anybody")
print("keep your password safe ")
Name = input("Enter your full Name :-")
len = int(input(" Enter the length of the password :--"))
complex = int(input("""enter the Complexity level 
                    1  LOW 
                    2 MEDIUM 
                    3 HIGH """))
if complex == 1:
    Character = string.ascii_lowercase+string.digits
elif complex == 2:
    Character= string.ascii_letters + string.punctuation + string.digits 
elif complex == 3:
    Character = string.ascii_letters + string.punctuation + string.digits + string.whitespace
else:
    print("Invaild complexity level \n Please Choose again!! ")

password = ''.join(random.choice(Character) for i in range(len))
print(f"{Name} Your Password is ", password )
print("THANK YOU ")
