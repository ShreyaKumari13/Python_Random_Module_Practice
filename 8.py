'''
    8. Write a Python program to create a list of random integers and randomly select multiple items from the said list. 
        Use random.sample()
'''
import random 
nums_list = random.sample(range(0,100), 10)
print(nums_list)
nums_selected_list = random.sample(nums_list,4)
print(nums_selected_list)