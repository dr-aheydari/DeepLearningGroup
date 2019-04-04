#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:58:06 2019

@author: aliheydari
"""
from __future__ import print_function, division
import os
import torch
import pandas as pd
#from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch.utils import data
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")


## Simple feed forward NN ##
class Net(nn.Module):
    
    def __init__(self, input_size, hidden_size, num_classes):
        # inherited from the parent class nn.Module
        super(Net, self).__init__()            
        # first layer of the full-connected Layer: 19163 [Inp] -> 100 
        # OR 19163 [inp] -> [however many hidden neurons you have]
        self.fc1 = nn.Linear(input_size, hidden_size) 
        # let's pick ReLU
        self.relu = nn.ReLU()                     
        # and if we need softmax
        self.softmax = nn.Softmax()
        
        # second full-connected layer: 100  [Hid Node] -> 2 [Binary Outp]
        self.fc2 = nn.Linear(hidden_size, num_classes) 
        
        ## HERE ^^ WE HAVE ROOM TO ADD MORE LAYERS IF WE WANT TO ##
    
    def forward(self, x):     
#        print(x.shape)
#        print("oh SHIT")
#        x = x.view(x.size(0), -1)     
                  
        # forward pass: stacking each layer together
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        
        ## here we would need more "out"s if we add more layers  in ^^ ##
        
        
        return out




## MAIN ##



# read the data
train_data = open("train_matrix.tsv", "r+");
#test_data = open("test_matrix.tsv", "r+");
test_data = open("val_matrix.tsv", "r+");

resp_data = open("train_response.tsv", "r+");
#test_resp_data = open("test_response.tsv", "r+");
test_resp_data = open("val_response.tsv", "r+");


# init the NUMPY arrays (later need tensors)
train = [];
tr_resp = [];
test = [];
tst_resp = [];
labels = [];

# use pandas to read the data and get rid of tabs
tr_df = pd.read_csv(train_data, sep="\t");   #  .tsv file into memory
ts_df = pd.read_csv(test_data, sep="\t");
tr_rs_df = pd.read_csv(resp_data, sep="\t",na_values=' ');

"""
NOTE: if you wanna use the code below, make sure to add the column headers to
the treatment response tsv file : )
    
"""
## we only need second column because second column has the 0 and 1 ##
tr_rs_df = tr_rs_df["COL2"];
ts_rs_df = pd.read_csv(test_resp_data, sep="\t");
ts_rs_df = ts_rs_df["COL2"];


# get only the numerical values of the arrays
train = tr_df.values;
test = ts_df.values;
train_resp = tr_rs_df.values;
test_resp = ts_rs_df.values;


### define hyper parameters

# input layer (rows of the matrix)
input_size = 19163 ;  

# num of hidden nodes of the hid. layer
hidden_size = 100      
# for now binary response output
num_classes = 2       

# an epoch is "the number of times entire dataset is trained"
num_epochs = 50
# the chuck of the input data we took for one iter
batch_size = 100    

# self adjusting alpha for the SGD or ADAM towards the end
learning_rate = 0.1

## ^^ this is something neat to mess around with ^^ ##


# turn NUMPY arrays to TENSORS
test_dataset = torch.from_numpy(test);
train_dataset = torch.from_numpy(train);
test_dataset.type(torch.FloatTensor);
train_dataset.type(torch.FloatTensor);

## these are the answers to responses that the patients had ##

# training labels
labels = train_resp; 
# testing labels
labels2 = test_resp; 
# turn to tensors
labels = torch.from_numpy(labels);
labels2 = torch.from_numpy(labels2);
# an absolutely useless step (redonded) but as a safty in case we forget WTF
resp_dataset = torch.from_numpy(train_resp);
test_resp_dataset = torch.from_numpy(test_resp);


# use pytorch's amazing data utilities
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                          batch_size=batch_size,
                                          shuffle=False);

## on purpose
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False);
# init NN
net = Net(input_size, hidden_size, num_classes);

# loss function
#criterion = nn.NLLLoss()
## cross entropy combines this ^^ and logSoftmax AND it works better
criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

#  let's try it with SGD
#optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

## RESULT: I needed to change the learning rate! I did not think it was such 
#   a big deal ... but it was! so SGD works great!
 
counter = 0;

### TRAIN ###
for epoch in range(num_epochs):
    
    # load a batch of our data
    for i,dat in enumerate(train_loader):  
        counter += 1;
        
        # convert TENSORS to VARIABLES for symbolic calculations
        dat = Variable(train_dataset.float())
        labels = Variable(labels)

        # init the hidden weights all zeros!
        optimizer.zero_grad()      
        # here we go: FORWARD pass                      
        outputs = net(dat)                                
        # compute the loss based on the criteria: our case cross entropy!!!
        loss = criterion(outputs, labels)          
        # here we go2: BACKWARD pass (and compute the weights!)
        loss.backward()                                   
        # optimizer: update the weights of hidden nodes
        optimizer.step()                                  
        
        # this is a step purely for printing out the steps
        if (i) % 322 == 0:                              
            # need to fix my math here... HELP!!!
#            print('Epoch [%d/%d], Step [%d/%d], Loss: %.4f'
#                 %(epoch+1, num_epochs, i + 1, len(train_dataset)//batch_size, loss.data))
             print('Epoch [%d/%d], Step [%d/%d], Loss: %.4f'
                 %(epoch+1, num_epochs, i + 1, len(train_dataset)//batch_size, loss.data))
        


### TEST ###


#### Just to make sure that the network is trained on the training data ####

correct = 0
total = 0

counter = 0
for dat in train_loader: 
    counter += 1;
    dat = Variable(train_dataset.float())
    outputs = net(dat)
    
    # choose the best class from the output --> The class with the best score
    _, predicted1 = torch.max(outputs.data, 1)
    # += the total count
    total += labels.size(0) 
    # += the total corrects!                 
    correct += (predicted1 == labels).sum()     # Increment the correct count
    
print('Accuracy of the network on the training data: %d %%' % (100 * correct / total))
#print("THIS ^^^ SHOULD BE 100%")
                        
#### the real testing step ####
        
correct = 0
total = 0
#
for dat in test_loader: 
    
    dat = Variable(test_dataset.float())
    outputs = net(dat)
     # choose the best class from the output --> The class with the best score
    _, predicted = torch.max(outputs.data, 1)  
     # += the total count
    total += labels2.size(0)  
     # += the total corrects!                     
    correct += (predicted == labels2).sum()     

print('Accuracy of the network on the test data: %d %%' % (100 * correct / total))
#print("THIS ^^^ SHOULD NOT BE 100% (unless I'm a god)")










