#! python3

# supertoss.py - A simple decision maker that takes
# a list of choices and randomly selects one.

import itertools
import time
import random
import sys

# get list of choices from terminal using pyinput plus

import pyinputplus as pyip

choices = []

while True:
    # keep entering choices until the user enters 'done'
    choice = pyip.inputStr('Enter a choice or enter done: ')
    if choice == 'done':
        break
    choices.append(choice)

spinner = itertools.cycle(['-', '/', '|', '\\'])

start_time = time.time()

while time.time() - start_time < 5:
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

# select a random choice

choice = random.choice(choices)

print('\nMy choice is: ' + choice)
