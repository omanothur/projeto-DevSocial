class Users:
    users = {}

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def register(cls):
        email_register = input('Email: ')
        if cls.is_valid_email(email_register):
            password_register = input('Password: ')
            cls.users[email_register] = {'email': email_register, 'password': password_register}
            print('User registered successfully!')
        else:
            print('This email is not valid!')
        print('-' * 10)

    @classmethod
    def login(cls, email, password):
        email_login = input('Email: ')
        password_login = input('Password: ')
        if email_login in cls.users and cls.users[email_login]['password'] == password_login:
            return print('Login successful!')
        else:
            return print('Login failed')

    @staticmethod
    def is_valid_email(email):
        return '@' in email
