# if elif else program in python 

# user email and password validation program
# User input Email id and password


email=input("enter the email id :- ")
if '@' in email:
    password=input('enter the password :- ')
    if email =='varad12@gmail.com' and password == '12345' :
        print('Welcome')
    elif email == 'varad12@gmail.com' and password != '12345':
        print('Password Incorrect')
        password=input('Enter the Password :- ')
        if password=='12345':
            print('Finally correct')
        else:
            print('sorry your wrong password')
    else:
        print('wrong Email and password')
else:
    print('email invalid')

# Phone validation program 

phone=input('Enter you phone name :-')
if phone == 'Iphone':
    print(f'{phone}  price is 30000 rs')
elif phone == 'vivo':
    print(f'{phone} price is 40000 rs')
else:
    print('phone is not availble')