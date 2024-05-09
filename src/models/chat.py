from src.models.users import Users


class Chat(Users):
    def __init__(self, email, password):
        super().__init__(email, password)

    @staticmethod
    def send_message(self, message):
        print(f"Sending message: '{message}'")

