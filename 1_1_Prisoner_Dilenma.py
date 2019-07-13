import os

"""
This is to simulate prisoner dilenma 
						Prisoner 2
					Confess		Deny
Prisoner 1 Confess	(X1, Y1) 	(X2, Y2)
		   Deny		(X3, Y3) 	(X4, Y4)
		   
In our current sample:
						Prisoner 2
					Confess		Deny
Prisoner 1 Confess	(-5, -5) 	(-1, -10)
		   Deny		(-10, -1) 	(-2, -2)
"""

#Prisoner 1
X1 = input("Get value of X1: ")
X2 = input("Get value of X2: ")
X3 = input("Get value of X3: ")
X4 = input("Get value of X4: ")

#Prisoner 2
Y1 = input("Get value of Y1: ")
Y2 = input("Get value of Y2: ")
Y3 = input("Get value of Y3: ")
Y4 = input("Get value of Y4: ")