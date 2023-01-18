#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:42:41 2022

@author: mehradhq
"""

import requests
import random
import string
word_site = "http://www.mieliestronk.com/corncob_lowercase.txt"

response = requests.get(word_site)
WORDS = response.content.splitlines()
chosen_word_byte=random.choice(WORDS)
chosen_word_str=str(chosen_word_byte)
chosen_word=""
for i in range (2,len(chosen_word_str)-1):
    chosen_word+=chosen_word_str[i]


length=len(chosen_word)
# print (chosen_word)

li=[]
for i in range (length):
    li.append("_")
for i in li:
    print (i,end=" ")

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


alphabet_string = string.ascii_lowercase
alphabet_list=list(alphabet_string)
class ANSI():
   def color_text(code):
        return "\33[{code}m".format(code=code)


guess_li=[]
counter=-1
while "_" in li:
    chances=6-counter
    print ("\n")
    print (f"you have {chances} chances left.")
    check_list=[]
    guess=input("guess a word:\n").lower()
    print ("the remaining letters are: ")
    for i in alphabet_list:
        if guess==i:
            alphabet_list.remove(i)
            break
    print (alphabet_list)
    for i in guess_li:
        if i==guess:
            print ("you have already used this letter")
            break
    else:
        print (ANSI.color_text(70)+"")
        guess_li.append(guess)
        
        for i in range (length):
            if chosen_word[i]==guess:
                li[i]=guess
                check_list.append(True)
            else:
                check_list.append(False)
        for j in check_list:
            if j==True:
                break
        else:
            counter+=1
            print (HANGMANPICS[counter])
        if counter==6:
            print ("you lose")
            print (chosen_word)
            break
        print ("\n")
        for j in li:
            print (j,end=" ")
else:
    print ("\nyou win")
            
            
    

    
