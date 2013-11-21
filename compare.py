import itertools

class CompareFeatures(object):
    def __init__(self, below50k, above50k):
        self.below50k = below50k
        self.above50k = above50k

    def Print(self):
        print self.below50k.title

    def Compare(self):
        self.average = (self.below50k.averageAge + self.above50k.averageAge)  / 2
        self.averageEducation = self.calAverage(self.below50k.averageEducation, self.above50k.averageEducation)
        self.averageCapitalGain = self.calAverage(self.below50k.averageCapitalGain, self.above50k.averageCapitalGain)
        self.averageCapitalLoss = self.calAverage(self.below50k.averageCapitalLoss, self.above50k.averageCapitalLoss)
        self.averageHoursPerWeek = self.calAverage(self.below50k.averageHoursPerWeek, self.above50k.averageHoursPerWeek)

        self.averageWorkClass = {}
        for f,b in itertools.izip_longest(self.below50k.averageWorkClass,self.above50k.averageWorkClass):
            self.averageWorkClass[f] = (self.below50k.averageWorkClass[f] + self.above50k.averageWorkClass[b]) / 2

        self.averageMaritialStatus = {}
        for f,b in itertools.izip_longest(self.below50k.averageMaritialStatus,self.above50k.averageMaritialStatus):
            self.averageMaritialStatus[f] = (self.below50k.averageMaritialStatus[f] + self.above50k.averageMaritialStatus[b]) / 2

    def calAverage(self, value1, value2):
        return (value1 + value2) / 2
