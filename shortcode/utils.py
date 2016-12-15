import random
import string

def shortener(size=6, chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for i in range(size))


def create_shortener(instance, )
