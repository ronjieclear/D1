#Dictionary are associative arrays, with key and values. values could be multiple
# a key could be a integer
# 
student = {'key':'value', 'courses':['Math','English','Filipino']}
student['key']='1'				#replace value
student.update({'key':'susi','age':26}) #update and could add keys at the end
# del student['age']				#delete the key together with its value
# print(student)					#display all the values of the set
# print(student['key'])  			#print value only
# print(student['courses'])  		#print value with apostrophies
# print(student.get('courses'))	#print value
# print(len(student)) 			#return the number of keys of a set
# print(len(student['courses'])) 	#return the number of values in a certrain key of a set

for key, value in student.items():
 	print(key, value)
