from models.User import User
from flask import jsonify
from config import db

def get_all_users():
    try:
        return [user.to_dict() for user in User.query.all()]    
    except Exception as error:
        print(f"ERROR {error}")

# -----------------------------------------------------------------------------------------------------
def create_user(name, email,last_name):
    try:
        new_user = User(name=name, email=email, last_name=last_name )
    
        db.session.add(new_user)
        db.session.commit()
        
        return new_user.to_dict()
    except Exception as e:
        print(f"ERROR {e}")

# -----------------------------------------------------------------------------------------------------
def update_user(user_id, name, email,last_name):
    try:
        user = User.query.get(user_id)
        if not user:
            return {"error": "Usuario no encontrado"}, 404

        user.name = name if name else user.name
        user.email = email if email else user.email
        user.last_name = last_name if last_name else user.last_name
        
        db.session.commit()
        return user.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500

# -----------------------------------------------------------------------------------------------------
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return {"error": "Usuario no encontrado"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "Usuario eliminado exitosamente"}, 200
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500
