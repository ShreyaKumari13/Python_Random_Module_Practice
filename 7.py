'''
    7. Write a Python program to generate a float between 0 and 1, inclusive 
        and generate a random float within a specific range. Use random.uniform()
'''
import random
print(random.uniform(0,1))
for i in range(5):
    print(random.uniform(1,3))

import random 
print("Generate a float between 0 and 1, inclusive:")
print(random.uniform(0, 1))
print("\nGenerate a random float within a range:")
random_float = random.uniform(1.0, 3.0)
print(random_float)
