# Backprop on the Seeds Dataset
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp
import math


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
	
	print(unique)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]    # {solved by l_unique}Classifier value varies depending on the first class detected
	print(lookup)
	return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	stats = [[min(column), max(column)] for column in zip(*dataset)]
	return stats

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	cc=0
	zz=0
	for row in dataset:
		for i in range(len(row)-1):
			#print("minmax1:{} \tminmax0:{} \tDiff:{}".format(minmax[i][1],minmax[i][0], minmax[i][1]-minmax[i][0]))
				#if minmax[i][1]!=minmax[i][0] they suggest to add if own data set to avoid 0 
				# if the same rows have same value it would retur 0
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
			#print(row[i])
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
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
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
		# print("----------------BACKPROP-----------S------------------------")
		# print(row)
		# print(prediction)				
		# print("----------------BACKPROP-----------E------------------------")
	# return(predictions)

	#working same as the result of back prop
	#however the problem is the normalization
	testing=[[0.7610953729933899, 0.8264462809917356, 0.5598911070780399, 0.7804054054054056, 0.6870990734141124, 0.4714532759494988, 0.7794190054160515, None],
	         [0.6128423040604343, 0.6136363636363638, 0.9056261343012707, 0.5253378378378378, 0.7505345687811829, 0.2848691310509824, 0.4751354012801576, None],
	         [0.4702549575070822, 0.566115702479339, 0.40471869328493637, 0.5748873873873874, 0.42836778332145387, 0.24378161203500245, 0.6696208764155587, None],
	         [0.014164305949008532, 0.0661157024793389, 0.22504537205081615, 0.13851351351351326, 0.008553100498930866, 0.5118906759937069, 0.21861152141802068, None],
	         [0.7610953729933899, 0.8264462809917356, 0.5598911070780399, 0.7804054054054056, 0.6870990734141124, 0.4714532759494988, 0.7794190054160515, None]]
	global bilang
	bilang+=1
	if bilang==5:
		predictions2 = list()
		for row in testing:
			#print(row)
			prediction2 = predict(network, row)  #row row
			predictions2.append(prediction2)	
			#print("----------------TESTING--------------S---------------------")
			#print(row)
			print(prediction2)				
			#print("----------------TESTING--------------E---------------------")

	return(predictions)
#----------------------------------------------------------------------------------------------------------------
def back_propagation2():
	# the duplicate works but return worng classification - fixed to #2
	network = initialize_network(7, 5, 3)

	testing=[[0.7610953729933899, 0.8264462809917356, 0.5598911070780399, 0.7804054054054056, 0.6870990734141124, 0.4714532759494988, 0.7794190054160515, None],
	         [0.6128423040604343, 0.6136363636363638, 0.9056261343012707, 0.5253378378378378, 0.7505345687811829, 0.2848691310509824, 0.4751354012801576, None],
	         [0.4702549575070822, 0.566115702479339, 0.40471869328493637, 0.5748873873873874, 0.42836778332145387, 0.24378161203500245, 0.6696208764155587, None],
	         [0.014164305949008532, 0.0661157024793389, 0.22504537205081615, 0.13851351351351326, 0.008553100498930866, 0.5118906759937069, 0.21861152141802068, None]]

	predictions2 = list()
	for row in testing:
		#print(row)
		prediction2 = predict(network, row)  #row row
		predictions2.append(prediction2)	
		print("----------------TESTING--------------S---------------------")
		print(row)
		print(prediction2)				
		print("----------------TESTING--------------E---------------------")
#----------------------------------------------------------------------------------------------------------------

def pasok():
	print("pasok")
	# predictions = list()
	# network = [7, 5, 3]
	testing=[[0.7610953729933899, 0.8264462809917356, 0.5598911070780399, 0.7804054054054056, 0.6870990734141124, 0.4714532759494988, 0.7794190054160515, None],
	         [0.7610953729933899, 0.8264462809917356, 0.5598911070780399, 0.7804054054054056, 0.6870990734141124, 0.4714532759494988, 0.7794190054160515, None]]
	print(type(testing))        
	print(type(network))   
	#for row in testing:		
	prediction = predict(network, testing[0])
	# 	predictions.append(prediction)
	print(row)
	print(prediction)
	# return(predictions)

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

# pasok()
# back_propagation2()

#predict() <-eto daw gamitin pra sa new values
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))




