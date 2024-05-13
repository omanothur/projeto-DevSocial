import re

class Users():  # Criação da classe
    users = {}

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def register(cls, email_register, password_register):
        if cls.is_valid_email(email_register):
            if cls.is_valid_password(password_register):
                if email_register not in cls.users:
                    cls.users[email_register] = {
                        'email': email_register,
                        'password': password_register
                    }
                    print('User registered successfully!')
                else:
                    print('This email is already registered.')
            else:
                print('Invalid password. Please use one longer than 8 characters.')
        else:
            print('Invalid email. Please check the email format.')


    @classmethod
    def login(cls, email, password):
        email_login = input('Email: ')
        password_login = input('Password: ')
        if email_login in cls.users:
            if cls.users[email_login]['password'] == password_login:
                print('Login successful!')
            else:
                print('Login failed(email or password is wrong)')
        else:
            print('This email does not exist...')

    @classmethod
    def is_valid_email(cls, email):
        # Use a more robust regex for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @classmethod
    def is_valid_password(cls, password):
        if len(password) >= 8:
            return True
        else:
            print('This password is not valid, try one longer than 8 characters')
            return False
