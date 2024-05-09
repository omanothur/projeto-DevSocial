
from time import sleep
import os
from src.models.chat import Chat
from src.models.users import Users


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
                email = input('Email: ')
                password = input('Password: ')
                user = Users(email, password)
                user.register(email, password)

            elif resposta == 2:
                try:
                    user = Users(email, password)
                    user.login(email, password)
                except UnboundLocalError as e:
                    print(f'{e}\nLoginError: You need to have a registration before logging in')


            elif resposta == 3:
                print('Thank tou for the company, come back often!')
                break
            sleep(4)
    menu()


    # chat_user = Chat(email='chat@example.com', password='securepassword')
    # Users.register(chat_user.email, chat_user.password)
    # chat_user.send_message("Olá, mundo!")

