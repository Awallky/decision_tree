# decision tree class
class dTree:
    def __init__(self, csvArr, numClasses, maxDepth, posRange):
        minV = 0
        maxV = 0
        minVFound = False
        maxVFound = False
        self.defineWhatIsPositive(posRange)
        self.maxDepth = maxDepth
        # num of fields to split on
        self.numFields = (len(csvArr[0])-1)
        # num of values to classify as
        self.numClasses = int(numClasses)
        # fields data
        self.fields = list()
        self.oracle = list()
        for i in range(0, self.numFields):
            self.fields.append(list())
        for row in csvArr:
            idx = 0
            for col in row:
                if idx < self.numFields:
                    self.fields[idx].append(col)
                else:
                    self.fields[idx].append(col)
                    self.oracle.append(col)
                idx += 1
        minV = self.oracle[0]
        maxV = self.oracle[0]
        for entry in self.oracle:
            if entry < minV:
                minV = entry
                minVFound = True
            elif entry > maxV:
                maxV = entry
                maxVFound = True
        self.minVal = minV
        self.maxVal = maxV
        self.thresholdVal = float((float(minV + maxV) / self.numClasses))
        self.threshold = list()
        for i in range(0, self.numClasses):
            tList = list()
            tList.append(float(self.minVal) + (float(i) * self.thresholdVal))
            tList.append(float(self.minVal) + (float(i+1) * self.thresholdVal))
            self.threshold.append(tList)
    def getTargetAttrs(self):
        targetAttrs = list()
        for i in range(0, self.numFields):
            targetAttrs.append(i)
        return targetAttrs
    def getExamples(self):
        return self.getAttrs()
    def getAttrs(self):
        return self.fields
    def defineWhatIsPositive(self, range):
        self.posRange = range
    def isPosRange(self, item):
        if (item >= self.posRange[0] and
            item <  self.posRange[1]):
            return True
        else:
            return False
    # id3(examples, target_attr, attrs, depth)
    # create root node for the tree 
    # if all examples are +, return label with +
    # if all examples are -, return label with -
    # if attrs is empty, return label from single node tree root
    # otherwise, do real work of id3:
    # pick the attribute that best classifies examples, i.e. the highest gain
    # set decision tree attr to a
    # for each possible value of a call them v[i], create a branch corresponding to the test A = v[i]
    # Let examples[v[i]] be the subset of examples that have hte value v[i] for A
    # If examples[v[i]] is empty assign it the  
    def runId3(self, examples, targetAttrs, depth):
        # create root node for the tree
        root = list()
        if depth >= self.maxDepth:
            return root

        num_pos = 0
        num_neg = 0
        num_total = 0
        for i in range(0, len(examples)):
            if self.isPosRange(examples[i][len(examples[i])-1]):
                num_pos += 1
            else:
                num_neg += 1
            num_total += 1
        # if all examples are +, return label with +
        if num_total == num_pos:
            root.append('+')
            return root
        # if all examples are -, return label with -
        elif num_total == num_neg:
            root.append('-')
            return root
        