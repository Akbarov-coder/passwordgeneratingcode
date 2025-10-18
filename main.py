# passwordgeneratingcode
import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_pass = int(input("Введите длину пароля:"))

password = ""

for i in range(len_pass):
    password += random.choice(symbols)

print(password)
