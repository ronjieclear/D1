# Backprop on the Seeds Dataset
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp
import math
import copy

bilang=0

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	l_unique=[]
	for itm in unique:
		l_unique.append(itm)	
	l_unique.sort(reverse=False)
	unique=[]
	for itm in l_unique:
		unique.append(itm)	
	
	#print(unique)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]    # {solved by l_unique}Classifier value varies depending on the first class detected
	#print("Class Assignment: {}".format(lookup))
	return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	stats = [[min(column), max(column)] for column in zip(*dataset)]
	#print(stats) #<- min max in each column
	return stats

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	cc=0
	zz=0
	#this function go through each cell of all dataset and normalize the value based on the min max of each column
	for row in dataset:
		for i in range(len(row)-1):
			#print("minmax1:{} \tminmax0:{} \tDiff:{}".format(minmax[i][1],minmax[i][0], minmax[i][1]-minmax[i][0]))
				#if minmax[i][1]!=minmax[i][0] they suggest to add if own data set to avoid 0 
				# if the same rows have same value it would retur 0
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
			#print(row[i]) #<-print individual value
			if (row[i])==0:
				zz+=1
				#print('zero {}'.format(zz))
				#ok - print("percent of zero in dataset: {0:.2f}%".format((zz/(zz+cc))*100) )				
			else:
				cc+=1


# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	#print("------------------Start Slipt-------------------")
	#print(dataset_split)   #result to 214 sets of value
	#print("-------------------END Slipt--------------------")
	return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None                            #<- removes the set class of test dataset
		predicted = algorithm(train_set, test_set, *args)  #<san galing ang likat na algorithm function??
		#print("xxxxxxxxxxxxxxS")
		#print(*args)  # value of args = 0.3 500 5
		#print("xxxxxxxxxxxxxxE")
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	# print(type(row))
	# print("row {} ".format(row))
	# print(type(network))
	# network is SET and LIST print("network {} ".format(network))
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)

# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)

# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	# print('ppppppppppppS')
	# print(network)	#<-could display the MODEL
	# print(row)	
	# print(outputs)	
	# print('ppppppppppppE')
	# sample result of outputs class not included
	# [0.0054060036098133825, 0.9922889248804062, 0.00018961887140228845] 
	#                              1                                     
    # [0.009587963933751914, 0.0011794266329153938, 0.993107155133636]
    #                                                   2
    # [0.6218966808985408, 0.6000506368824172, 0.00017178789188091012]
    #         0
    # this is run 215 times the dataset is 210 + 5 testing dataset
	#-ok print(outputs.index(max(outputs))) #<-return the 0, 1 or 2 the resutlt classifier
	return outputs.index(max(outputs))

# Backpropagation Algorithm With Stochastic Gradient Descent
def back_propagation(train, test, l_rate, n_epoch, n_hidden):
	n_inputs = len(train[0]) - 1  #nabibilang ang attributes
	n_outputs = len(set([row[-1] for row in train]))  #nabibilang kung ilan ang classes
	network = initialize_network(n_inputs, n_hidden, n_outputs)
	
	#print("in{} hide{} out{}".format(n_inputs, n_hidden, n_outputs))##############
	# why 5x pumapasok sa back propagation

	train_network(network, train, l_rate, n_epoch, n_outputs)
	predictions = list()
	for row in test:
		prediction = predict(network, row)  #row row
		predictions.append(prediction)	
	return(predictions)
#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

def direct():
	print('-----------------R E S U L T   S T A R T-----------------')
	filename_ko = 'seeds_dataset_test.csv'
	dataset_ko = load_csv(filename_ko)  
	# dataset_ko=[
	# 			['15.26','14.84','0.871','5.763','3.312','2.221','5.22','1'],
	# 			['17.12','15.55','0.8892','5.85','3.566','2.858','5.746','2'],
	# 			['16.63','15.46','0.8747','6.053','3.465','2.04','5.877','1'],
	# 			['18.27','16.09','0.887','6.173','3.651','2.443','6.197','2'],
	# 			['11.56','13.31','0.8198','5.363','2.683','4.062','5.182','3'],
	# 			['12.3','13.34','0.8684','5.243','2.974','5.637','5.063','3']
	# 			]
	dataset_orig = copy.deepcopy(dataset_ko)
	for i in range(len(dataset_ko[0])-1):
		str_column_to_float(dataset_ko, i) 
	str_column_to_int(dataset_ko, len(dataset_ko[0])-1)
	
	normalize_dataset(dataset_ko, minmax)

	nett=[[{'weights': [1.5261865922546158, 0.24323582411800948, 0.41086127149905133, -10.210894951294394, 2.971618428613504, 4.829452837378416, 8.482266135864739, -2.930164292063065], 'output': 0.8353085738105864, 'delta': -1.6668142756760569e-06}, {'weights': [5.645862290503782, 4.39844579859114, -1.0265985077134054, -7.672538827771478, 4.04632845224292, 4.373217175387437, 7.485387111523629, -8.922428615371018], 'output': 0.9578503488282164, 'delta': -2.8033099606451573e-10}, {'weights': [5.105345173323351, 5.446511942724408, -0.4912655858010164, 9.01239716633781, 1.122037737753915, 0.2812377580432156, -13.301553363686505, -1.3795067674428845], 'output': 0.9866358285755943, 'delta': 3.5104085927662727e-06}, {'weights': [1.0121048667102934, 1.0565761290555027, -0.6075916292848027, 0.558380406776694, 2.239710688150816, 0.630850933442254, 4.283128402215938, -0.7259248385713641], 'output': 0.9979499447996072, 'delta': -1.2059055225281552e-06}, {'weights': [5.18187887257841, 5.395353598927418, 0.11020442723693302, 5.216500814551704, 3.68156811329991, -1.2355632063506787, -1.060985454954308, -5.0684242316927115], 'output': 0.9998135716482487, 'delta': 2.58417694359122e-06}], [{'weights': [-7.576522409412085, -10.804628951006134, 11.441908258951015, -2.693384314173221, 2.538895156854417, 0.3235715007517538], 'output': 0.0054060036098133825, 'delta': 3.6007146172173457e-07}, {'weights': [6.289831046658422, 8.369299518716346, -1.168708022511552, -4.41715542146618, 4.399536177133271, -7.250656329101941], 'output': 0.9922889248804062, 'delta': -9.60148482147022e-09}, {'weights': [6.931419160916442, -2.0721449833677537, -9.72853009967772, 2.8684517401492484, -5.8225761799395865, 0.1820619244556481], 'output': 0.00018961887140228845, 'delta': -1.8611535175932023e-06}]]	
	roww=dataset_ko

	c=0
	for i in roww:
		roww[c][-1] = None
		c+=1
	c=0
	for rowwin in roww:
		outputs = forward_propagate(nett, rowwin)
		predictedresult=outputs.index(max(outputs))
		print("Data:{} \tResult:{}".format(dataset_orig[c],predictedresult))
		c+=1

	print('-----------------R E S U L T   E N D -----------------')


#----------------------------------------------------------------------------------------------------------------
# Test Backprop on Seeds dataset
seed(1)
bilang=0
# load and prepare data
filename = 'seeds_dataset.csv'
dataset = load_csv(filename)    #array|set of csv 

for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)    #convert string cell value to float

# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

# normalize input variables
minmax = dataset_minmax(dataset)

normalize_dataset(dataset, minmax)

# evaluate algorithm
n_folds = 5
l_rate = 0.3
n_epoch = 500
n_hidden = 5

scores = evaluate_algorithm(dataset, back_propagation, n_folds, l_rate, n_epoch, n_hidden)

direct()
# pasok()
# back_propagation2()

#predict() <-eto daw gamitin pra sa new values
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))




