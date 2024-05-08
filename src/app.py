from src.utils.Users import Users

email = input('Email: ')
password = input('Password: ')

user = Users(email, password)

Users.register(email, password)

Users.login(email, password)

print(vars(user))
