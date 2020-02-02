# Decision Tree Class Definition
import numpy as np

class dTree(object):
  def __init__(self, trainData):
    self.trainData = trainData[:]
    self.trainDataAttrs = list()
    for i in range(0, len(self.trainData)-1):
      self.trainDataAttrs.append(i)
    self.oracleArr = np.transpose(self.trainData[len(self.trainData)-1]).tolist()
    self.entropy = 1.0
    self.maxSplits = 3 # to be decided by config file later
    self.numSplits = 0
  def getEntropy(self):
    ret = 0.0
    err = 0
    
    return err, ret
  def getGain(self):
    ret = 0.0
    err = 0
    
    return err, ret
  def isPos(self, examples)
  def runID3(self, examples, targetAttr, listOfAttrs):
    err = 0
    # create root node for dTree
    root = list()
    numPos = 0.0
    numNeg = 0.0
    numTotal = 0.0
    for example in examples:
      if(self.isPos(example)):
        numPos += 1.0
      else:
        numNeg += 1.0
      numTotal += 1.0
    # If all examples are +, return the single-node tree Root with the + label 
    if numPos == numTotal:
      root = ['+', None]
    # If all examples are -, return the single-node tree Root with the - label 
    elif numNeg == numTotal:
      root = ['-', None]
    # If number of predicting attributes is empty, then return the single node
    #   tree Root, with label most commonly occuring value of the target attr in the examples
    elif not listOfAttrs:
      if numPos >= numNeg:
        return ['+', None]
      else:
        return ['-', None]
    # Else, begin the real work:
    else:
      pass
    #   A <- attribute that best classifies the set of examples
    #   Decision tree atribute for root = A
    #    For each possible value, v[i], of A,
    #      Add a new tree branch root below Root, corresponding to the test v[i] == A
    #      If Examples[ v[i] ] is empty,
    #        then below this new branch, add a leaf node with label = most common target value in the examples
    #      Else, below this new branch add the subtrree ID3(Examples[ v[i] ], targetAttribute, set of attributes in A)
    return err, root