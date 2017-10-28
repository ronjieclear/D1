print('Sucessfully imported my_module')

test = 'Test string'						#a sample variable that can be use when imported

def find_index(to_search, target):
	'''Hanapin the index of a value in a sequence'''
	for i, value in enumerate(to_search):   #enumerate() <- a function that add counter
		if value == target:
			return i 						# return index location if found
	return -1								# return -1 if not found