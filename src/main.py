from src.models.chat import Chat
from src.models.users import Users

if __name__ == "__main__":
    email = input('Email: ')
    password = input('Password: ')
    user = Users(email, password)

    user.register(email, password)

    user.login(email, password)

    # chat_user = Chat(email='chat@example.com', password='securepassword')
    # Users.register(chat_user.email, chat_user.password)
    # chat_user.send_message("Olá, mundo!")
