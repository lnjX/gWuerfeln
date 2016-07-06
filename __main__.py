#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Guenther - Wuerfeln
Copyright (C) 2016 LNJ <git@lnj.li>
WTFPL, See <http://www.wtfpl.net/txt/copying> for more information.
"""

import random
from time import sleep

def main():
	print("Guenther - Wuerfeln")
	print("Copyright (C) 2016 LNJ <git@lnj.li>\n")
	
	print("Hallo, ich bin Guenther und ich wuerfele immer mit zwei Wuerfeln.")
	
	wuerfelungen = int(input("Wie oft soll ich wuerfeln? "))
	sleeptime = float(input("Wie lange soll ich nach jeder Wuerfelung warten? "))
	
	endResult = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
	
	
	print("\n| 2\t| 3\t| 4\t| 5\t| 6\t| 7\t| 8\t| 9\t| 10\t| 11\t| 12 \t|")
	print("=========================================================================================")
	
	for i in range(1, wuerfelungen):
		cube1 = random.randint(1, 6)
		cube2 = random.randint(1, 6)

		result = cube1 + cube2

		endResult[result] += 1
		
		print("|", endResult[2], "\t|", endResult[3], "\t|", endResult[4], "\t|", endResult[5], "\t|", endResult[6], "\t|",
		endResult[7], "\t|", endResult[8], "\t|", endResult[9], "\t|", endResult[10], "\t|", endResult[11], "\t|",
		endResult[12], "\t|", end="\r")
		
		sleep(sleeptime)
	
	print("\n\nBYE. BYE.")

main()
