import re


def validate_phone_number(phone_number):
    pattern = r"^(?:\+7|8)[0-9]{10}$"
    if re.match(pattern, phone_number):
        return True
    else:
        return False
