import random
import string
pass_len = 12
charv = string.ascii_letters + string.digits + string.punctuation
passw = ""
'''for i in range(pass_len):
    passw += random.choice(charv)
print(f'''"\nYour andom Password is: \n{passw}"
res = "".join([random.choice(charv) for i in range(pass_len)])
print(res)