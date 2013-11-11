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

        self.capitalGain = 0
        self.averageCapitalGain = 0
        self.capitalLoss = 0
        self.averageCapitalLoss = 0
        self.hoursPerWeek = 0
        self.averageHoursPerWeek = 0

        self.count = 0

        self.totalAge = 0
        self.averageAge = 0

        self.totalEducation = 0
        self.averageEducation = 0

    def assign(self, line):
        self.workClass[line[1]] += 1
        self.maritialStatus[line[5]] += 1
        self.occupation[line[6]] += 1
        self.relationship[line[7]] += 1
        self.race[line[8]] += 1
        self.sex[line[9]] += 1

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

    def averageWorkClass(self, line):
        self.workClass[line[1]] += 1

    def assignTotals(self, line):
        self.totalAge += int(line[0])
        self.totalEducation += int(line[4])
        self.capitalGain += int(line[10])
        self.capitalLoss += int(line[11])
        self.hoursPerWeek += int(line[12])

    def takeFeatures(self, line):
        self.incrementCount()
        self.assign(line)
        self.assignTotals(line)

def main():
    below50k = Features("below50k")
    above50k = Features("above50k")

    with open("textfile.txt", 'rb') as f:
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


    print above50k.title
    print "Average Age: " ,above50k.getAverageAge()
    print "Average Work Class: " ,above50k.getAverageEducationClass()

if __name__ == '__main__':
    main()
