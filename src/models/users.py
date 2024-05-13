class Users():  # Criação da classe
    users = {}
    emails_valid = ['@hotmail.com', '@gmail.com', '@yahoo.com']

    def __init__(self, email, password):
        self.email = email
        self.password = password


    @classmethod
    def register(cls, email_register, password_register):
        if cls.is_valid_email(email_register):
            if cls.is_valid_password(password_register):
                cls.users[email_register] = {
                        'email': email_register,
                        'password': password_register
                    }
                print('User registered successfully!')
            else:
                print()


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
        for valid_email in cls.emails_valid:
            if email.endswith(valid_email):
                if email in cls.users:
                    print('This email is already being used, try another one.')
                    return False

                return True
        print('This email is not valid! Check if it matches the email pattern')
        return False

    @classmethod
    def is_valid_password(cls, password):
        if len(password) >= 8:
            return True
        else:
            print('This password is not valid, try one longer than 8 characters')
            return False
