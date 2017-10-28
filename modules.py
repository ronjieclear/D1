#MODULES
courses = ['Social Studies', 'Math', 'English', 'Physics'] 

import sys   			# the system? 
## sys.path.append('C:\D1\D1\moduleloctst')	#absolute path is needed
sys.path.append('moduleloctst')	#<- name of the folder which contain the module. a folder inside this folder
# print(sys.path) 		# shows the list of directory where Python look for libraries/modules


#the module that will be import should be in the same directory

##Ways to import and call modules or function

# 1.> Basic way to import and call module
# import my_module   
# index = my_module.find_index(courses,'Math')   			
# print(index)

# 2.> Assign the module to a variable to make it an object
# import my_module as mm 						
# index = mm.find_index(courses,'English')   			
# print(index)

# 3.> Direct import of function in a module / cons: other function are not imported
# from my_module import find_index
# index = find_index(courses,'Physics')
# print(index)

# 4.> Direct import + asign to variable and import other variable or function
# from my_module import find_index as fi,test
# index = fi(courses,'Physics')
# print(test)

# call and send value to the function of the imported module; and assign to variable

# print(index)
# displays 2 because English is in index 2


##Built in Module|Library
import random
rand_course = random.choice(courses)
print(rand_course)

import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
today = datetime.date.today()
print(today)

import calendar
year =2020
print(calendar.isleap(2020))

print('The year {} is {} Leapyear'.format(year,calendar.isleap(year)))

import os
print(os.getcwd()) #-get current working directory
# other function could, scan, delete, create files and others
print(os.__file__)    #- __ double underscore means dondoer? shows the location of the library


import webbrowser
site=input("enter website")
webbrowser.open('http://{}.com'.format(site))
print('the site is {}'.format(site))