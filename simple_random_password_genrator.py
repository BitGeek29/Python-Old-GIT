import random 
import string

total = string.ascii_letters + string.digits + string.punctuation

lenght = 16

password = "".join(random.sample(total,lenght))
print(password)