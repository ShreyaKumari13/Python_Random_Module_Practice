'''
    1. Write a Python program to generate a random color hex, a random alphabetical string, random value 
        between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()
'''
import random
import string
print("Generate a random value between two integers, inclusive:")
print(random.randint(0,3))
print(random.randint(-7,7))
print("Generate a random multiple of 7 between 0 and 70:")
print(random.randint(0,10)*7)
s=''
for i in range(10):
    s+=random.choice(string.ascii_letters)
print("Generate a random string")
print(s)
print("Generate a random color hex: ")
print("#{:06x}".format(random.randint(0,0xFFFFFF)))
