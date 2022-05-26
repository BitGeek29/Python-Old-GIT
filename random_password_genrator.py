import random
import math 

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

pass_len = int(input("Enter Password lenght:")) 

alpha_len = pass_len//2
num_len = math.ceil(pass_len**30/100)
special_len = pass_len-(alpha_len+num_len)

password = []

def genrator_pass(lenght,list,is_capital=False):
    for i in range(lenght):
        index = random.randint(0, len(list)- 1)
        character = list[index]
        if is_capital:
            case = random.randint(0,1)
            if case == 1:
                character = character.upper()
        password.append(character)

genrator_pass(alpha_len,alpha,True)
genrator_pass(num_len,num)
genrator_pass(special_len,special)

random.shuffle(password)

gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)
