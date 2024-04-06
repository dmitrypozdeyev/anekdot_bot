import json


class User:
    def __init__(self, username, chatid):
        self.username = username
        self.chatid = chatid
        self.is_subscribe = False
        self.new = True
        self.register()

    def register(self):
        try:
            with open('auth.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}
        if self.username in users:
            self.new = False
            self.chatid = users[self.username]['chatid']
            self.is_subscribe = users[self.username]['subscribe']
        else:
            users[self.username] = {'chatid': self.chatid, 'subscribe': self.is_subscribe}
            self.new = True
        
        
        with open('auth.json', 'w') as f:
            json.dump(users, f, indent=4)        
    
    def subscribe(self):
        self.is_subscribe = True
        with open('auth.json', 'r') as f:
            users = json.load(f)
        users[self.username]['subscribe'] = True
        with open('auth.json', 'w') as f:
            json.dump(users, f, indent=4)
            
    def unsubscribe(self):
        self.is_subscribe = False
        with open('auth.json', 'r') as f:
            users = json.load(f)
        users[self.username]['subscribe'] = False
        with open('auth.json', 'w') as f:
            json.dump(users, f, indent=4)
            

            
def subscribed_users():
    with open('auth.json', 'r') as f:
        users = json.load(f)
        for user in users:
            if users[user]['subscribe']:
                yield User(user, users[user]['chatid'])