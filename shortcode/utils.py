import random
import string

def shortener(size=6, chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for i in range(size))


def create_shortener(instance, size=6):
	newcode = shortener(size=size)
	Klass = instance.__class__
	qs = Klass.objects.filter(short=newcode).exists()
	if qs:
		return shortener(size=6)
	return newcode
