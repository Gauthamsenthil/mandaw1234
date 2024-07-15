correct= "Gautham@1234"

password = ""

while password !=correct:
    password=input("enter your password")
    if password==correct:
        print("ACCESS GRANTED!!")
    else:
        print("ACCESS DENIED!!")
print("you have successfully unlocked your password")