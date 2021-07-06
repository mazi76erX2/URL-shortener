import random
import string


def create_random_string():
    url_string = string.ascii_letters + string.digits

    return ''.join(random.choice(url_string) for i in range(6))
