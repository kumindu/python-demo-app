class User(object):
    def __init__(self,id,name,username,password):
        self.id = id
        self.name=name
        self.username = username
        self.password = password

    def __str__(self):
        return self.name

