import numpy as np
import random

size = int(input()) #array size defined by user input
content = ['x','.'] #to be randomized accross the array
matrix = np.zeros((size,size), dtype = object) #create a defined array, fill with 0
flag = 0 #loop breaker

#===========================
# randomizing and checking
#===========================

while not flag == 1:
	flag = 0 #reset by each loop

#randoming array element

	for i in range(0,size):
		for j in range(0,size):
			matrix[i][j] = random.choice(content)

#check if it's meet the condition;
#- All values in 2-d array are either ‘X’ or ‘.’
#- At least one cell separates any two lines
#- There are no adjacent lines
#- There are no diagonal lines*
#bassicaly, we just need to make sure there is no diagonal x's inside the array

for y in range(1,size):
	for x in range(1,size):
		if (matrix[y][x]=='x') and (matrix[y-1][x-1]=='x'):

		#uncomment to see matched diagonal lines
		#print("diagonally match",y,",",x,"-",y-1,",",x-1)
			flag -= 1
		elif (matrix[y-1][x]=='x') and (matrix[y][x-1]=='x'):
		#print("diagonally match",y-1,",",x,"-",y,",",x-1)
			flag -= 1
if flag == 0: #change into 1 so it's break from while loop
	flag = 1
	break

#=======================
# counting total line
#=======================

line = 0
for x in range(0,size): # count horizontal line and single node
	for y in range(0,size):
		if x == 0:
			if (matrix[x,y] == 'x') and (matrix[x+1,y] != 'x'):
				if y == 0:
					line+=1
				else:
					if matrix[x,y-1] == '.':
						line+=1
		elif (x>0) and (x<size-1):
			if (matrix[x,y] == 'x') and (matrix[x-1,y] != 'x') and (matrix[x+1,y] != 'x'):
				if y == 0:
					line+=1
				else:
					if matrix[x,y-1] == '.':
						line+=1
		elif x == size-1:
			if (matrix[x,y] == 'x') and (matrix[x-1,y] != 'x'):
				if y == 0:
					line+=1
				elif y > 0:
					if matrix[x,y-1] == '.':
						line+=1
for x in range(0,size): # count vertical line
	for y in range(0,size):
		if y == 0:
			if (matrix[x,y] == 'x') and (matrix[x,y+1] != 'x'):
				if x == 0:
					line+=1
				elif x < size-1:
					if (matrix[x-1,y] == '.') and (matrix[x+1,y] != '.'):
						line+=1
		else:
			if (matrix[x,y] == 'x') and (matrix[x,y-1] != 'x'):
				if x == 0:
					if (matrix[x+1,y] != '.'):
						line+=1
			elif x < size-1:
				if (matrix[x-1,y] == '.') and (matrix[x+1,y] != '.'):
					line+=1

#======================
# printing result
#======================

print(size,'x',size,"cartesian spaces\n")

for i in range(0,size):
	print(" ".join(str(x) for x in matrix[i]))

print("\ntotal line(s)",line)