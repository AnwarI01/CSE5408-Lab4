# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:04:39 2023

@author: luisg
Luis Garcia 
CSE5408 Lab04

"""
#Write a program containing a function to reverse a user 
#inputted string. [start:stop:step]
def Reverse(x):
    print("Here is the reveresed string:\n",x[::-1])

user_input = input("Enter a string : ")

print("Here is the Original word:\n",user_input)
Reverse(user_input)
