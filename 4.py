'''
    4. Write a Python program to construct a seeded random number generator, 
    also generate a float between 0 and 1, excluding 1. Use random.random()
'''
import random
print("Construct a seeded random number generator:")
for i in range(5):
    # print(random.Random(0).random())
            #or
    random.seed(10)
    print(random.random())
print("Generate a float between 0 and 1, excluding 1:")
print(random.random())
