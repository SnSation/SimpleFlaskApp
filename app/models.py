from datetime import datetime as dt

class User:
    def __init__(self, _id, first_name, last_name, email):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f'<User: [{self.id}] {self.first_name} {self.last_name}>'

class Post:
    def __init__(self, _id, body):
        self.id = _id
        self.body = body
        self.created_on = dt.utcnow()

    def __repr__(self):
        return f'<Post: [{self.id}] {self.body}>'