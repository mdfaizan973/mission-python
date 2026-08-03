import string

def check_password(password):
    upper = any(ch.isupper() for ch in password)
    lower = any(ch.islower() for ch in password)
    digit = any(ch.isdigit() for ch in password)
    special = any(ch in string.punctuation for ch in password)

    message = "Correct Password!"
    status = True

    if len(password) < 6:
        message =  "Password must be at least 6 characters long."
        status = False

    if not upper:
        message = "Password must contain at least one uppercase letter."
        status = False

    if not lower:
        message = "Password must contain at least one lowercase letter."
        status = False

    if not digit:
        message = "Password must contain at least one digit."
        status = False

    if not special:
        message =  "Password must contain at least one special character."
        status = False

    return {
        "message": message,
        "status": status
    }
