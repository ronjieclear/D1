#FUNCTIONS
# def f_hello():   	# to declare a function the def followed by the dunction name, () and colon
# 	pass			# this states that the function have nothing to do. just to avoid error

# print(f_hello) 		# output - <function f_hello at 0x0000000000492EA0>  name and loc of function
# print(f_hello())		# execute the function the output is None

# def f_hello():
# 	print('Subject')	#pass is removed because the function have content

# f_hello()				# use to call and execute the funtion

# def f_add(x,y):			#function parameters
# 	total=x+y
# 	return '{} + {} = {}'.format(x,y,total)		#return value even if it string. format function is good!

# print(f_add(2,3))


# def f_add(x,y=10):			#function parameters could be hardcoded  but could be overrided
# 	total=x+y
# 	return '{} + {} = {}'.format(x,y,total)		#return value even if it string. format function is good!

# # print(f_add(2))				# missing parameters is accepted if it has given value
# print(f_add(2,3))				# parameters is overriden if a there parameters are complete


def f_studinfo(*args, **kwargs):	# *args could contain multiple tupple  **kwargs could contain multiple sets
"""DOCSTRING a functions description... """
	print(args)						# displays ('Math', 'English', 'Filipino')
	print(kwargs)					# displays {'name': 'John', 'course': 'BSIT'} 

# f_studinfo('Math', 'English', 'Filipino', name='John', course='BSIT') #*args value first before the **kwargs
# OUTPUT
# ('Math', 'English', 'Filipino')
# {'name': 'John', 'course': 'BSIT'}

courses = ['Math', 'English', 'Filipino']
info = {'name': 'John', 'course': 'BSIT'}
# f_studinfo(courses,info)
# the output is different because the variable is place inside another parentheses
# (['Math', 'English', 'Filipino'], {'name': 'John', 'course': 'BSIT'})
# {}

# to correct it an asterisk should be place to unpack the value inside the variables 
# f_studinfo(*courses,**info)
# output is below
# ('Math', 'English', 'Filipino')
# {'name': 'John', 'course': 'BSIT'}


