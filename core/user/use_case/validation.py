def validate(password, username, name, email, user_type):
    if not password or not username or not name or not email or not user_type or len(password) < 8 or user_type == "admin":
        return False
    else: 
        return True

    

