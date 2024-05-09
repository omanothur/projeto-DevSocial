class Users():  # Criação da classe
    users = {}
    emails_valid = ['@hotmail.com', '@gmail.com', '@yahoo.com']

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def register(cls, email_register, password_register):  # Método para fazer o registro do usuário!

        if cls.is_valid_email(email_register):
            if cls.is_valid_password(password_register):
                cls.users[email_register] = {'email': email_register, 'password': password_register}
                print('User registered successfully!')
            else:
                print('This email or password is not valid!\nTry a valid email or a larger password...')
        print('-' * 10)

    @classmethod
    def login(cls, email, password):  # Método para fazer o login, de acordo se as credenciais estão corretas
        email_login = input('Email: ')
        password_login = input('Password: ')
        if email_login in cls.users and cls.users[email_login]['password'] == password_login:
            return print('Login successful!')
        else:
            return print('Login failed')

    @classmethod
    def is_valid_email(cls, email):  # Método para verificar se o 'Email' realmente é um email
        for valid_email in cls.emails_valid:
            if email.endswith(valid_email):
                return True
        return False

    @classmethod
    def is_valid_password(cls, password):
        if len(password) >= 8:
            return True
        else:
            return False
