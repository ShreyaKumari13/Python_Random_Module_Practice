'''
    3. Write a Python program to generate a random alphabetical character, alphabetical 
        string and alphabetical string of a fixed length. Use random.choice()
'''
import random
import string
s = random.choice(string.ascii_letters)
print("Generate a random alphabetic character")
print(s)
print("Generate a random alphabetical string:")
max_length = 50
str1 = ""
for i in range(random.randint(1, max_length)):
    str1 += random.choice(string.ascii_letters)
print(str1)
a=""
for i in range(10):
    a+=random.choice(string.ascii_letters)
print("Generate a random alphabetical string of fixed length:")
print(a)