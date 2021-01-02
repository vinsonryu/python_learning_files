Username = ['banana']
Password = ['apple']

q1 = input("do you have a account")

def login():
    if q1 == "y":
        username = input("enter username")
        password = input("enter password")
        iofu = Username.index(username)
        if iofu == Password.index(password):
            print("Login successful")
        else:
            q3 = input("username or password incorrect.Do you want to try again? (y/n)\n")
            if q3 == 'y':
                login()
            elif q3 == 'n':
                print("ok bye")
            else:
                print("you've choose to do nothing bye.")
login()
if q1 == "n":
    q2 = input("do you want to create acc")
    if q2 == "y":
        new_username = input("enter username")
        new_password = input("enter password")
        Username.append(new_username)
        Password.append(new_password)
        print("your acc has been registered\n")
        q4 = input('Do you want to login? (y/n)\n')
        if q4 == 'y':
            q1 = 'y'
            print(q1)
            login()
        elif q4 == 'n':
            print("ok bye")
        else:
            print("you've choose to do nothing bye.")
else:
    print("you've choose to do nothing bye.")

print(Username)
