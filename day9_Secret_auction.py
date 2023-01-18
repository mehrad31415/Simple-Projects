#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 10:05:06 2022

@author: mehradhq
"""

import os
clear = lambda: os.system('clear')


print ("""
        ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      
""")

print ("Welcome to the secret auction program")
dic={}
repeat="yes"
while repeat=="yes":
    name=input("What is your name?:\n")
    bid=int(input("What's your bid?:\n$"))
    dic[name]=bid
    repeat=input("are there any other bidders? type 'yes' or 'no'. ")
    clear()
    while repeat!="yes" and repeat!="no":
        repeat=input("you can only choose yes or no!: ")
maximum=max(dic.values())
for i in dic:
    if dic[i]==maximum:
        print (f"{i} is the winner of the secret auction. ")
