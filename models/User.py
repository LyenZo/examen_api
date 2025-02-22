from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable= False)
    email = db.Column(db.String(50), unique= True, nullable= False)
    last_name = db.Column(db.String(50), nullable= False)
    
    def __init__(self, name, email,last_name ):
        self.name = name
        self.email = email
        self.last_name = last_name
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "last_name": self.last_name,
        }
        
    
    