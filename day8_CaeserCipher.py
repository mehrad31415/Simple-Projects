#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:13:33 2022

@author: mehradhq
"""

"""
This is is caeser cipher program:
"""

#getting the three inputs
repeat="yes"
while repeat=="yes":
    choose=input("do you want to encode or decode:\n").lower()
    if choose!="decode" and choose!="encode":
        print ("we have no other options!")
    else:
        word=input("what is your chosen word?\n")
        shift=int(input("how many shifts do you want to give?\n"))
    
        #below gives a list of the alphabets
        import string
        alphabet=list(string.ascii_lowercase)
        
        #in decode we shift the other way around
        if choose=="decode":
            shift=-shift
         
        new_word=""
        for i in word:
            if i==" ":
                new_word+=" "
                continue
            new_index=alphabet.index(i)+shift
            if new_index>25:
                new_index=new_index%26
            elif new_index<0:
                nex_index=new_index+26
            new_word+=alphabet[new_index]
        
        print (new_word)
    repeat=input("do you want to go again, yes or no:\n")
    
    
    
        
        