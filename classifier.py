import contextlib
import sys
from collections import defaultdict

class Features(object):

    def __init__(self, name):
        self.title = name
        self.workClass = defaultdict(int)
        self.educationNumber = defaultdict(int)
        self.maritialStatus = defaultdict(int)
        self.occupation = defaultdict(int)
        self.relationship = defaultdict(int)
        self.race = defaultdict(int)
        self.sex = defaultdict(int)
        self.capitalGain = defaultdict(int)
        self.capitalLoss = defaultdict(int)
        self.hoursPerWeek = defaultdict(int)

        self.totalAge = 0
        self.count = 0
        self.averageAge = 0
        self.test = 0

    def assign(self, line):
        self.age[line[0]] += 1
        #self.workClass[line[1]] += 1
        self.educationNumber[line[4]] += 1
        self.maritialStatus[line[5]] += 1
        self.occupation[line[6]] += 1
        self.relationship[line[7]] += 1
        self.race[line[8]] += 1
        self.sex[line[9]] += 1
        self.capitalGain[line[10]] += 1
        self.capitalLoss[line[11]] += 1
        self.hoursPerWeek[line[12]] += 1

    def incrementCount(self):
        self.count = self.count + 1

    def getAverageAge(self):
        return self.totalAge / self.count

    def averageValue(self, line):
        self.totalAge += int(line[0])

    def averageWorkClass(self, line):
        self.workClass[line[1]] += 1

    def takeFeatures(self, line):
        self.incrementCount()
        self.averageValue(line)

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
    print below50k.totalAge
    print below50k.count
    print below50k.getAverageAge()

    print above50k.title
    print above50k.totalAge
    print above50k.count
    print above50k.getAverageAge()

if __name__ == '__main__':
    main()
