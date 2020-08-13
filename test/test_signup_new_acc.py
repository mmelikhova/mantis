import string
import random


def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_signup_new_account(app):
    username = random_username("mln_", 10)
    password = "milena"
    app.james.ensure_user_exists(username, password)