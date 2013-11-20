import sys
import features
import recordAttributes

class CompareFeatures(object):
    def __init__(self, below50k, above50k):
        self.below50k = below50k
        self.above50k = above50k
        self.result = recordAttributes.RecordAttributes()

    def Print(self):
        print self.below50k.title

    def Compare(self):
        self.average = (self.below50k.averageAge + self.above50k.averageAge)  / 2
        self.averageEducation = self.calAverage(self.below50k.averageEducation, self.above50k.averageEducation)
        self.averageCapitalGain = self.calAverage(self.below50k.averageCapitalGain, self.above50k.averageCapitalGain)
        self.averageCapitalLoss = self.calAverage(self.below50k.averageCapitalLoss, self.above50k.averageCapitalLoss)
        self.averageHoursPerWeek = self.calAverage(self.below50k.averageHoursPerWeek, self.below50k.averageHoursPerWeek)

    def calAverage(self, value1, value2):
        return (value1 + value2) / 2
