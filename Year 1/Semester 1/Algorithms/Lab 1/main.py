import sys
from arabic_to_roman import *
from roman_to_arabic import *

thing = input()

# checking for input
if thing=="":
	sys.exit("Missing input")

# check if input is a number
try:
	a_in = int(thing)
	if a_in<=3000 and a_in>=1:
		to_roman(a_in)
	else: 
		print("Number must be between 1 and 3000")

# input is a string
except:
	r_in=thing.upper()
	allowed=set("MDCLXVIN")
	if set(r_in).issubset(allowed):
		to_arabic(r_in)
	else:
		print("Wrong input")