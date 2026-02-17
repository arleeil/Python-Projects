class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0



user_1 = User('001','angela')
user_1.follower = 45

user_2 = User('002','lee')
print(user_1.name )
