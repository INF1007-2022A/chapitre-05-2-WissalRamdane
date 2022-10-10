#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib2to3.pgen2.token import NEWLINE
import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	somme=0
	
	for produit in data:
		somme+=produit[INDEX_QUANTITY ]* produit[INDEX_PRICE]

	taxes=(somme*15)/100
	total=somme+taxes
	person=input('Enter yout name :')

	bill_data = [("SOUS TOTAL", somme, "$"), 
                 ("TAXES", taxes, "$"),
                 ("TOTAL", total, "$")]

	print(person,bill_data)
	


def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
