#Gonzalo Birrueta
#9-4-19 CS 1.1
#Spaceman

import time
from termcolor import colored, cprint
import sys

#This printFlush function makes it possible to make scrolling text, which makes the program a little more interactive:)
def printFlush(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.075)

def welcome_msg():
    printFlush("Welcome to Spaceman!\n")

welcome_msg()
