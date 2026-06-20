
ACCOUNTS = {
    "admin@example.com": "h4ckm3",
}


def check_login(email, password):
    """ Checks whether the specified credentials are valid """
    return ACCOUNTS.get(email) == password