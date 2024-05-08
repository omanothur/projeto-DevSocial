users = {}


def register():
    email = input('Email: ')
    password = input('Password: ')
    print('User registered successfully!')
    users[email] = {'email': email, 'password': password}
    print('-' * 10)


def login():
    email_login = input('Email: ')
    password_login = input('Password: ')
    if email_login in users and users[email_login]['password'] == password_login:
        print('Login successful!')
    else:
        print('Login failed')


register()
login()

