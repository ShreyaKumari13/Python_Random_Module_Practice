'''
    5. Write a Python program to generate a random integer between 0 and 6 - excluding 6, 
    random integer between 5 and 10 - excluding 10, random integer between 0 and 10, with a 
    step of 3 and random date between two dates. Use random.randrange()
'''
import random
import datetime
print(random.randrange(0,7))
print(random.randrange(5,10))
print(random.randrange(0,10,3))
start_time = datetime.date(2020,7,21)
end_time = datetime.date(2021,7,21)
time_between_days = end_time-start_time
days_between_dates = time_between_days.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_time + datetime.timedelta(days=random_number_of_days)
print(random_date)
