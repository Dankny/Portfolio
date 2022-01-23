# This is a simple voucher code generator
# It's used as it named. To make a voucher code

import string
import random

# Set the size_letters for how many letters characters do you want to generate randomly
# Set the size_num for how many numbers characters do you want to generate randomly
def id_generator_split(size_letters=5, size_num=2, letters=string.ascii_uppercase, num=string.digits):
    letters = ''.join(random.choice(letters) for _ in range(size_letters))
    nums = ''.join(random.choice(num) for _ in range(size_num))
    # The output will be like, XYZAW14 or QWERT53
    return letters + nums

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    # The output will be like, BQS9Z3 or UHRVPU
    return ''.join(random.choice(chars) for _ in range(size))

# Can make hundreds or thousands and more of the code, but manually copy it from terminal
for i in range(0, 1000):
    print(id_generator())