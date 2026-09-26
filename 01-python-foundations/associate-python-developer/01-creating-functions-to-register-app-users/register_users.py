def validate_user(name, email, password):
    if not validate_name(name):
        raise ValueError("the name should be greater than two characters and is a string data type.")
    if not validate_email(email):
        raise ValueError("Checks that the email address is in a valid format, has a username greater than 1 character, an '@' symbol, and an allowed domain that is in the `top_level_domains` variable.")
    if not validate_password(password):
        raise ValueError("Checks that the password is strong enough. It should include a capital letter, a number between 0-9 and be greater than 8 characters.")
    return True


def register_user(name, email, password):
    try:
        valid_dict = validate_user(name, email, password)
    except:
        return False
    return {"name": name, "email": email, "password": password}


register_user("alia", "alex@alexdomin.com", "kjqsd#lK21LKS")
