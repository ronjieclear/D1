#LOOPS

nums = [1,2,3,4,5]
lets = ['a','b','c','d','e']

# for num in nums:
# 	if num == 3:
# 		print('found!')
# 		# break #skip the itteration and the whole for
# 		continue # just skip one iteration so #3 is not printed
# 	print(num)

# for num in nums:
# 	for letter in 'abcd':
# 		print(str(num)+'-'+(str(letter)).upper())

# x='123'
# y=len(nums)
# z=11
# for i in range(y,z):
# 	print(i)

# x=0
# while False:
# 	if x==999999:
# 		break
# 	print(x)
# 	x +=1




#1A
#2A
#2B
#3A
#3B
#3C



# for n in range(1,len(nums)):
# 	for d in range(0,n):
# 		print(n,lets[d])

#1A
#1B
#1C
#1D
#2A
#2B
#2C
#3A
#3B
#4A

# x=len(nums)
# for n in range(1,x):
# 	y=len(nums)
# 	x=x-1	
# 	z=0
# 	for l in range(n,y):
# 		print(n,lets[z])
# 		y=y-1
# 		z=z+1


# 5A
# 4A
# 4B
# 3A
# 3B
# 3C
# 2A
# 2B
# 2C
# 2D
# 1A
# 1B
# 1C
# 1D
# 1E

# x=1
# for n in range(len(nums),0,-1):#loop backward
# 	for l in range(0,x): 
# 		txt=(str(n)+(lets[l]).upper())
# 		print(txt)
# 	x=x+1

############# WHILE LOOP
# x=0

# while x <= 10:
# 	if x == 5:
# 		print('Found')
# 		break
# 	print(x)
# 	x+=1

x=0
while True:
	if x== 5:
		break
	print(x)
	x=x+1
# infinite loop use 90% of the CPU even ESC key is press to end/hide the output. 
# to solve the issue the program should be re run with a corrected loop
