#Conditional Statements
#	Operators
#	is  	Test if the location of the variable is same as the another NOT exact value
#	is		Object Identity
#	==		Equal
#	!=		Not Equal
#	>		Greater Than
#	<		Less Than
#	>=		Greater or Equal
#	<=		Less or Equal


language = 'Javascript'

if language == 'Phyton':
	print('Language is Phyton')			# no open bracket need just indention
elif language == 'Java':				# rather than use else of it is just elif
	print('Language is JavA')			
elif language == 'Javascript':
	print('Language is JavAScript')	
else:
	print('No match')


if True:								# even though there are no condition the statement
	print('Test True')					# could return true, once assigned true
										# variables are automatically detected to test to true

user = 'admin'
logged_in = 'true'						# even 'True' or 'true' is accepted small non apo true is not

if user == 'admin' and logged_in:
	print('Admin Page')
else:
	print('Invalid Page')

print('----------')

logged_in= False
if not logged_in:						# not operator check bool value if it is False
	print('Please log in')
else:
	print('Welcome')

print('-----------')
#Bool values that return FALSE
#	False
#	None
#	0
#	Empty list, set, tupple
#	Empty dictionary 

condition = 0
if condition:
	print('Evaluated True')
	print('Another Line of True')
else:
	print('Evaluated False')
	print('Another Line of False')


