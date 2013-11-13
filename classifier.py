from __future__ import division
import contextlib
import sys
from collections import defaultdict


class Features(object):

    def __init__(self, name):
        self.title = name
        self.workClass = defaultdict(int)
        self.maritialStatus = defaultdict(int)
        self.occupation = defaultdict(int)
        self.relationship = defaultdict(int)
        self.race = defaultdict(int)
        self.sex = defaultdict(int)

        self.totalAge = 0
        self.averageAge = 0
        self.totalEducation = 0
        self.averageEducation = 0
        self.capitalGain = 0
        self.averageCapitalGain = 0
        self.capitalLoss = 0
        self.averageCapitalLoss = 0
        self.hoursPerWeek = 0
        self.averageHoursPerWeek = 0

        self.averageWorkClass = 0
        self.averageMaritialStatus = 0
        self.averageOccupation = 0
        self.averageRelationship = 0
        self.averageRace = 0
        self.averageSex = 0

        self.count = 0

    def assignDiscreteTotals(self, line):
        self.workClass[line[1]] += 1
        self.maritialStatus[line[5]] += 1
        self.occupation[line[6]] += 1
        self.relationship[line[7]] += 1
        self.race[line[8]] += 1
        self.sex[line[9]] += 1

    def assignNumericTotals(self, line):
        self.totalAge += int(line[0])
        self.totalEducation += int(line[4])
        self.capitalGain += int(line[10])
        self.capitalLoss += int(line[11])
        self.hoursPerWeek += int(line[12])

    def incrementCount(self):
        self.count = self.count + 1

    def getAverageAge(self):
        return self.totalAge / self.count

    def getAverageEducationClass(self):
        return self.totalEducation / self.count

    def getAverageCapitalGain(self):
        return self.capitalGain / self.count

    def getAverageCapitalLoss(self):
        return self.capitalLoss / self.count

    def getAverageHoursPerWeek(self):
        return self.hoursPerWeek / self.count

    def calculateDiscreteAverages(self):
        self.averageOccupation = 0
        self.averageRelationship = 0
        self.averageRace = 0
        self.averageSex = 0

        self.averageWorkClass = {}
        for k,v in self.workClass.iteritems():
            self.averageWorkClass[k] = v / self.count
            print self.averageWorkClass[k]

        self.averageMaritalStatus = {}
        for k,v in self.maritialStatus.iteritems():
            self.averageMaritalStatus[k] = v / self.count
            print self.averageMaritalStatus[k]

    def takeFeatures(self, line):
        self.incrementCount()
        self.assignDiscreteTotals(line)
        self.assignNumericTotals(line)


def main():
    below50k = Features("below50k")
    above50k = Features("above50k")

    with open("sample.txt", 'rb') as f:
        for line in f:
            feature = line.split(',')
            outcome =  feature[14].rstrip()
            if (outcome == ' <=50K'):
                below50k.takeFeatures(feature)
            if (outcome == ' >50K'):
                above50k.takeFeatures(feature)

    print below50k.title
    print "Average Age: " ,below50k.getAverageAge()
    print "Average Work Class: " ,below50k.getAverageEducationClass()
    print below50k.workClass.items()
    print "Below50k Count:" ,below50k.count
    print below50k.maritialStatus.items()

    print above50k.title
    print "Average Age: " ,above50k.getAverageAge()
    print "Average Work Class: " ,above50k.getAverageEducationClass()
    print above50k.workClass.items()
    print "Above50k Count:" ,above50k.count

    below50k.calculateDiscreteAverages()

if __name__ == '__main__':
    main()
