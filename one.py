import random
import string

length = 10
letters = string.ascii_letters + string.digits
rand_string = ''.join(random.choice(letters) for i in range(length))
print(rand_string)
