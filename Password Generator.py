import random
Lower = "abcdefghijklmnopqrstuvwxyz"
Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = '0123456789'
SYMBOL = '[]{}#()*;._-'

ALL = Lower + Upper + NUMBER + SYMBOL
Length=12
Password = "".join(random.sample(ALL,Length))
print("The Generated Password is :- ",Password)
