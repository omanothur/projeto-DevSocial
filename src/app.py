from src.utils.Users import Users

if __name__ == "__main__":
    email = ''
    password = ''
    user = Users(email, password)

    user.register()

    user.login(email, password)

    print(vars(user))
