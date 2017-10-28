# LIST is Array in python
courses = ['Social Studies', 'Math', 'English', 'Physics'] #-index also starts at 0

#just realize, PYTHON generate error if there are improper indention

# print(courses) # print all the value of the list complete with bracket and comma
# print(courses[0]) # print the first value of list
# print(courses[-1]) #print the last value of the list
# print(courses[2:]) # print multiple value of the list in range / slicing 1:3 |:3 | 3:

courses.append('Art') #- add new value to last index
courses.insert(1,'Filipino') #insert value to a specified index

## 2D list / array
# courses2 =['Education', 'Art']# new list
# courses.insert(1,courses2) #insert list inside a list 2D array
## output ['Social Studies', ['Education', 'Art'], 'Filipino', 'Math', 'English', 'Physics', 'Art']

### MERGE LIST through extend function
kurso = ['PE', 'ICT', 'Art'] 
courses.extend(kurso) 
#-add individual value of a list to another list INSERTION INDEX NOT suported
## output  added at last
## output ['Social Studies', 'Filipino', 'Math', 'English', 'Physics', 'Art', 'Education', 'Art']

### remove and POP
# courses.remove('PE') #remove a value from the list
# removeditem = courses.pop(0) #remove vlaue from the list and assign it to a variable withou apostrophe
# print(courses)
# print(removeditem)


## reverse & sort
# courses.reverse() #-return list in reverse mode
## sort
# courses.sort(reverse=True) #sort by alphabetical order or numerical order sort(reverse=True) to Z-A 
##however this function alter the order of the list realtime and in memory
##print(help(list.sort))
## -the original list wont be affected. declare and sort the new list
# newSortList = sorted(courses,reverse=True) 
# print(newSortList)


## min max len sum
# numList = [1,3,5,8,2,4]
# print(numList)
# print(min(numList))
# print(max(numList))
# print(len(numList))
# print(sum(numList))


### seach and return index location of the first value
# print(courses.index('Art')) $ there are two Art in the list 
# print(courses.index('Art'))
## Question? How to find the next Art in the List
# x = ('Math' in courses) # search if there are Math in the list and return bool
# print(x)
## shorthand print('Math' in courses) 


## LIST LOOP
# for subj in courses:  	# this will loop through the entire list. notice a colon at the end. 
# 	print(subj)       	#indented that says its under the loop. declate new var subj as looper
# 						# return items line by line without apostrophy

# for pos, subj in enumerate(courses): 	# enumerate add another looper that could extract another value
# 	print(pos, subj)					# print two variables Index and Value

# for pos, subj in enumerate(courses, start=1): 	# add start in index IT JUST OVERIDE THE 0 index to 1
# 	print(pos, subj)					# print two variables Index and Value

#Question? how to start in a given value let say Math

####   FAILED to start at certain index
# x = courses.index('Art')
# print(x) 
# for pos, subj in enumerate(courses, start=1): 	# add start in index
	# print(pos, subj)					# print two variables Index and Value

# return the list as single string seperated by a certain character in this example  "-"
# course_str = ' - '.join(courses)
# print(course_str)
### output Social Studies - Filipino - Math - English - Physics - Art - PE - ICT - Art   


#read list in a string and generate a new list    str>array
# course_str = ' x '.join(courses)
# print(course_str)
# new_list = course_str.split(' x ') 	#spaces in left and right of the X ensures that the value 
# 									#that will be saved in the array dont have space
# print(new_list)

#list are mutable it means; a list is assign to another when the first list is updated the 
#secon will also be updated even thought it is not re assign

#LIST
# array = ['Filipino', 'English', 'Math']   #<- this is a LIST 		mutable		- can be modify	
#TUPLES
# array = ('Filipino', 'English', 'Math')   #<- this is a TUPLES  	unmutable	- cant be modify
#DICTIONARY
# array = {'name':'Jhon','subjects':'Filipino', 'English', 'Math'}   #<- this is DICTIONARY
#SETS
# array = {'Filipino', 'English', 'Math', 'English'}   #<- this is a SETS		- randomly print values
#																				- remove duplicates		
# list is optimize for comparing and union, find difference and intersection

is_courses = {'PPS','Analytics','IISP','Math'}
it_courses = {'PPS','CSOMT','Networking','Math'}

# print(is_courses.intersection(it_courses)) 	# shows only the common value among sets
# print(is_courses.difference(it_courses)) 		# shows unique value present on the first set
# print(is_courses.union(it_courses))			# combine the both sets

# creating empty lis 
# list1 =[]
# list2 = ()
# list3 = set()
# list3.add('Filipino')
# list3.add('ENGLISH')
# print(list3)
 