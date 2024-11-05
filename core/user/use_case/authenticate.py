from core.user.models import User


def authenticate(email):
    if User.objects.filter(email=email).exists:
        return True
    else:
        return False