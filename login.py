class Login:
    def __init__(self) -> None:
        while True:
            userName = input("Username: ")
            if (userName.isspace() != True):
                break
        while True:
            password = input("Password: ")
            if (password.isspace() != True):
                break
