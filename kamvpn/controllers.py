def valid_login(username, password):
    if username == 'admin' and password == 'q1w2e3r4t5':
        return True
    else:
        return False


def log_the_user_in(username):
    return 'Welcome ' + username
