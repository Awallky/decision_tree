import numpy
import math

# decision tree class
class dTree:
    def __init__(self, csvArr, numClasses, maxDepth):
        self.gain = 1.0 
        self.maxDepth = int(maxDepth)
        # num of fields to split on
        self.numFields = (len(csvArr[0]))
        # num of values to classify as
        self.numClasses = int(numClasses)
        # fields data
        self.posRanges = list()
        self.minVals = list()
        self.maxVals = list()
        self.thresholds = list()
        self.fields = numpy.transpose(csvArr).tolist()
        self.defineWhatIsPositive()
    # get target attributes [0, n-1] from the fields data member
    def getTargetAttrs(self):
        targetAttrs = list()
        for i in range(0, self.numFields-1):
            targetAttrs.append(i)
        return targetAttrs
    def getExamples(self):
        return self.getAttrs()
    def getAttrs(self):
        return self.fields
    def defineWhatIsPositive(self):
        # for every attribute, define the +/- value
        for i in range(len(self.fields)):
            minV = float(min(self.fields[i]))
            thresh = 0
            l = self.fields[i]
            for idx in range(0, len(l)):
                thresh += float(l[idx])
            thresh = float(thresh / len(l))
            thresholds = list()
            for i in range(0, self.numClasses):
                thresholds.append([minV+(i*thresh),
                                 minV+((i+1.0)*thresh)])
            self.posRanges.append(thresholds)
    def isPosRange(self, targetAttr, item):
        MIN_AVG_RANGE_IDX = 0
        MIN_V_IDX = 0
        AVG_V_IDX = 1
        if (float(item) > float(self.posRanges[targetAttr][MIN_AVG_RANGE_IDX][MIN_V_IDX]) and
            float(item) < float(self.posRanges[targetAttr][MIN_AVG_RANGE_IDX][AVG_V_IDX])):
            return True
        else:
            return False
    def getGain(self, examples, targetAttr):
        num_pos   = 0
        num_neg   = 0
        num_total = 0
        for i in range(0, len(examples[targetAttr])):
            if self.isPosRange(len(examples[0])-1, examples[len(examples[0])-1][i]):
                num_pos += 1
            else:
                num_neg += 1
            num_total += 1
        pos_ratio = (num_pos/num_total)
        neg_ratio = (num_neg/num_total)
        entropy = -(pos_ratio)*math.log(pos_ratio) - (neg_ratio)*math.log(neg_ratio)
        return entropy
    # id3(examples, target_attr, attrs, depth)
    # create root node for the tree 
    # if all examples are +, return label with +
    # if all examples are -, return label with -
    # if attrs is empty, return label from single node tree root
    # otherwise, do real work of id3:
    # pick the attribute that best classifies examples, i.e. the highest gain
    def runId3(self, examples, targetAttr, attrs, depth):
        # create root node for the tree
        root = list()
        if depth >= self.maxDepth:
            return root
        depth += 1
        num_pos = 0
        num_neg = 0
        num_total = 0
        for i in range(0, len(examples)):
            if self.isPosRange(len(examples[0])-1, examples[len(examples[0])-1][i]):
                num_pos += 1
            else:
                num_neg += 1
            num_total += 1
        # if all examples are +, return label with +
        if num_total == num_pos:
            print(1)
            root.append(['+', targetAttr])
            return root
        # if all examples are -, return label with -
        elif num_total == num_neg:
            print(2)
            root.append(['-', targetAttr])
            return root
        # if attrs is empty, return label from single node tree root
        elif(len(attrs) == 0):
            if num_pos >= num_neg:
                print(3)
                root.append(['+', targetAttr])
            else:
                print(4)
                root.append(['-', targetAttr])
            return root
        # otherwise, do real work of id3:
        else:
            # pick the attribute that best classifies examples, i.e. the highest gain
            examples
            maxG = 0.0
            maxI = 0
            for i in range(0, len(attrs)):
                tmp = self.gain - self.getGain(examples, i)
                if(tmp > maxG):
                    maxG = tmp
                    maxI = i
            # set decision tree attr to a
            removeList = list()
            for i in range(0, len(examples[maxI])):
                if not self.isPosRange(maxI, examples[maxI][i]):
                    removeList.append(i)
            for i in range(0, len(removeList)):
                for attrIdx in range(0, len(examples[0])):
                    print(removeList[i], examples[attrIdx])
                    examples[attrIdx].pop(removeList[i])
            # for each possible value of a call them v[i],
            # create a branch corresponding to the test A = v[i]
            # Let examples[v[i]] be the subset of examples that have the value v[i] for A
            # If examples[v[i]] is empty assign it the
            print(5)
            return root
