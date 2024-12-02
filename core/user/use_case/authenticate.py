from core.user.models import User

def authenticate(email):
    try:
        user_exists = User.objects.get(email=email)
        return user_exists
    except User.DoesNotExist as error:
        return None

