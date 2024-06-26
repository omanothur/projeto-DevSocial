from time import sleep
from src.models.chat import Chat
from src.models.users import Users
import os


if __name__ == "__main__":
    def menu():
        while True:
            print("\nOpções:" +
                  "\n1. Cadastro" +
                  "\n2. Fazer login" +
                  "\n3. Sair")
            print('-' * 10)
            resposta = int(input())
            if resposta == 1:
                email = input('Register email: ')
                password = input('Register password : ')
                user = Users(email, password)
                user.register(email, password)

            elif resposta == 2:
                try:
                    user = Users(email, password)
                    user.login(email, password)
                except UnboundLocalError as e:
                    print(f'{e}\nLoginError: You need to have a registration before logging in')

            elif resposta == 3:
                print('Thank you for the company, come back often!')
                break
            else:
                print('There is no such option, please try a valid one.')
            sleep(2.5)
    menu()


