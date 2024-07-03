import random

alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,"
upper_alphabets = alphabets.upper()
numbers = "1,2,3,4,5,6,7,8,9,0,"
symbols = ".,;,/,',\",},{,[,],},-,=,+,_"

total = alphabets+upper_alphabets+numbers+symbols

characters = total.split(",")


def password_gen(length):
    password = ""
    for i in range(length):
        chosen = random.choice(characters)
        password = password + chosen
    return password

required_length = int(input("Enter length of required password:"))

generated_password = password_gen(required_length)

print(f"The random password of length {required_length} characters is: {generated_password}")


    