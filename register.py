from entities.user import User

class Register:

    symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

    def __init__(self) -> None:
        
        while True:
            firstName=input("Name: ")
            if(firstName.isalpha()==True):
                break
        while True:
            lastName=input("Last Name: ")
            if(lastName.isalpha()==False):
                break
        while True:
            userName=input("Username: ")
            if(userName.find(" ")==-1):
                break
        while True:
            password=input("Password: ")
            if(password.find(" ")==-1 and not any(char.isupper() for char in password) and not any(char.islower() for char in password) and not any(char.isdigit() for char in password) and not any(char in self.symbols for char in password)):
                break
        user=User(firstName,lastName,userName,password)
        self.register(user)



    def register(user:User):
        print(user.firstName,"kayit basarili")