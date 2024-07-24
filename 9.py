'''
    9. Write a Python program to set a random seed and get a random number between 0 and 1. Use random.random.
'''
import random 
print("Set a random seed and get a random number between 0 and 1:")
for i in range(5):
    random.seed(0)
    print(random.random())
    random.seed(1)
    print(random.random())
