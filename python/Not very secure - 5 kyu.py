import string
def alphanumeric(password: str) -> bool:
    return bool(password) and all(c in string.ascii_letters + string.digits for c in password)
