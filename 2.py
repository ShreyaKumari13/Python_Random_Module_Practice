'''
    2. Write a Python program to select a random element from a list, set, 
        dictionary (value) and a file from a directory. Use random.choice()
'''
import random
import os 
list1 = [1,2,3,"shreya"]
tuple1 = (1,2,3,4,"shreya")
dict1 = {1:"shreya",2:"navneet",3:"sona"}
set1 = {1, 2, 3, 4}
print(random.choice(list1))
print(random.choice(tuple1))
print(random.choice(dict1))
print(random.choice(tuple(set1)))
print(random.choice(os.listdir())) #this provides directories insine the open folder 
print(random.choice(os.listdir("/"))) #this provides directory of file from the system or outside of this folder all over the system