import random
import os

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*-_=+;:,.<>'
password = ''

length = int(input('How long should the password be? '))
service = str(input('For which service will you use the password? '))
for i in range (length):
    password += random.choice(chars)
print (password)

passwords = open ('Passwords.txt', 'a+')
passwords.write (service +' ' + password + '\n')