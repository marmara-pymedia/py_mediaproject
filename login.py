from register import Register

class Login:
    def __init__(self) -> None:
        request=input("Kayit?: ")
        if(request=="y"):
            register=Register()
        elif(request=="n"):
            while True:
                userName=input("Username: ")
                if(userName.isspace()!=True):
                    break
            while True:
                password=input("Password: ")
                if(password.isspace()!=True):
                    break
            
            print("Login!")

