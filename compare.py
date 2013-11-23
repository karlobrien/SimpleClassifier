from __future__ import division
from collections import defaultdict
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

        self.averageMaritialStatus = defaultdict(int)

        for e in self.below50k.averageMaritalStatus:
            self.averageMaritialStatus[e] += self.below50k.averageMaritalStatus[e]

        for e in self.above50k.averageMaritalStatus:
            self.averageMaritialStatus[e] += self.above50k.averageMaritalStatus[e]


    def calAverage(self, value1, value2):
        return (value1 + value2) / 2
