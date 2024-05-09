from src.utils.Users import Users

if __name__ == "__main__":
    email = input('Email: ')
    password = input('Password: ')
    user = Users(email, password)

    user.register(email, password)

    user.login(email, password)


