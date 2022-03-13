letters = "asdfghjklzxcvbnmqwertyuiop"
letter = list(letters)
upper_case_letters = letters.upper()
upper_case_letter = list(upper_case_letters)
symbols ='''
        ~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/
        '''
numbers = "1234567890"

password_lenght = 0
lowercase = 0
Uppercase = 0
special = 0
numeric = 0
integrity = 0

while integrity < 4:
    password = input("enter password: ")
    if len(password) < 8:
        print("password must be have atleast 8 characters")
    for character in password:
        if character in letters:
            lowercase = 1
        elif character in upper_case_letters:
            Uppercase = 1
        elif character in symbols:
            special = 1
        elif character in numbers:
            numeric = 1

    integrity = lowercase + Uppercase + special + numeric
    if lowercase != 1:
        print("need a lower case charceter")
    elif Uppercase != 1:
        print("need an upper case charceter")
    if special != 1:
        print("need a special charceter")
    if numeric != 1:
        print("need a numerical chaacter")
    elif integrity == 4:
        print("great password")



#if number not in password:
#print("f")
#password_size = len(password)
#min_password_size = 8

