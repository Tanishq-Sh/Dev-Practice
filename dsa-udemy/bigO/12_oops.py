class Youtube:
    
    def __init__(self, name, subscribers=0, subscriptions=0):
        self.name = name
        self.subscribers = subscribers
        self.subscriptions = subscriptions
        
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1
        

user1 = Youtube("Tanishq")
user2 = Youtube("Cherry")
user3 = Youtube("Rahul")

user1.subscribe(user2)
user3.subscribe(user2)

print(f"{user1.name} subscibers {user1.subscribers}")
print(f"{user1.name} subscriptions {user1.subscriptions}")

print(f"{user2.name} subscibers {user2.subscribers}")
print(f"{user2.name} subscriptions {user2.subscriptions}")
        