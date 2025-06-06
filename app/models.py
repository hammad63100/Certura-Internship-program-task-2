# In-memory user store with hashed passwords
from werkzeug.security import generate_password_hash, check_password_hash

users = {
    'testuser': generate_password_hash('testpass')
}

def check_user_password(username, password):
    if username in users:
        return check_password_hash(users[username], password)
    return False
