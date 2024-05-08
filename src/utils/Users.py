class Users:
    users = {}

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def register(cls, email, password):
        print('User registered successfully!')
        cls.users[email] = {'email': email, 'password': password}
        print('-' * 10)

    @classmethod
    def login(cls, email, password):
        email_login = input('Email: ')
        password_login = input('Password: ')
        if email_login in cls.users and cls.users[email_login]['password'] == password_login:
            return print('Login successful!')
        else:
            return print('Login failed')
