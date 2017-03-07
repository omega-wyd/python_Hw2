#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 student1 <student1@CS3030_87>
#
#===========================================================================
#
#       File:Micheal_Brewer_Hw2 
#
#       Usage: ./Micheal_Brewer_Hw2
#
#   Description: This script is written in python to simulate how an ATM would
#                   ask for a pin and check top see if it is the correct pin.
#
#       Options: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         Notes: ---
#        AUTHOR: Micheal Brewer 
#        EMAIL:  mbrewerramirez@mail.weber.edu
#  ORGANIZATION: 
#       CREATED: 2017-03-03 14:45
#      REVISION:  3-6-2017
#===========================================================================
import sys

pin = input

def check(pin):
    """
    Check the PIN of the input if it equals 1234
    ARGS: 
        pin -> user input
    Returns
        true or false
    """
    if pin == '1234':
        return True
    else:
        return False

def length(pin):
    """
    check for proper legnth of pin
    ARGS: pin -> user input
    Return:
        None
    """
    if len(pin) != 4:
        print(" Invalid PIN lenth. Correct format is: <9876>")
        return


def num(pin):
    """
    Check if pin is only numbers.
    ARGS:
        pin -> user input
    Returns:
       None 
    """
    if pin.isnumeric() == False:
        print(" Invalid PIN character. Correct format is: <9876>")

def gitInput(pin):
    """
    Run Pin through full testing testing
    ARGS:
        pin -> user input
    Return:
        Accept PIN or Decline
    """
    attempts = 0
    while attempts < 3:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if check(pin):
            print("Pin accepted!")
            return True
            break
        else: 
            print("Your Pin is incorrect")
            attempts = attempts + 1
            #print("attempt #" attempts)    # Check that attempts is incrementing correctly
            length(pin)
            num(pin)
    print("Your bank card is blocked")
    return False

#Main Function
def main():
    """
    Ask for users PIN checks for authenticity
    Allows three attempts before ending session and locking card.

    USAGE:
        python3 Micheal_Brewer_Hw2.py
        ./Micheal_Brewer_Hw2.py
   """
    
    gitInput(pin)


if __name__=="__main__":
    # Call Main
    main()
    exit(0)
