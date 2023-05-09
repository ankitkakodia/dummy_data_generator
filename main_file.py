import setting
from db_setup import *
from datetime import datetime
import random
import string
import hashlib
import dummy_data_generator_functions as dd


print('''
Welcome to dummy generator....
Please select your action.
1. to add dummy user
2. to add dummy product
3. to add dummy transaction''')

action = int(input('Please enter your action: '))

if (action == 1):
    num = int(input('Enter number of users: '))
    for user_data in range(num):
        dd.generate_name()
    print('User Data Added')
elif (action == 2):
    num = int(input('Enter number of Products: '))
    for product_data in range(num):
        dd.generate_product()
    print('Products Added')
elif (action == 3):
    dd.generate_transaction()
    
    









