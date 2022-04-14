class User:

    def __init__(self, user_id, username):
        print(f'new user "{username}" being created...')
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "Lukas")
print(user_1.id)
user_2 = User("002", "Caro")

print(user_2.followers)