"""
Lab: 3
Version: 1.0
Dev: Kuroedov Danila
Date: 24.03.2024
"""

import random

def gen(len: int):
    '''Function for init list by generator'''
    current = random.random()
    count = 0
    while count < len:
        count += 1
        yield current
        current += random.random()
        