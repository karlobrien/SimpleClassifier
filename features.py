from __future__ import division
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

        #self.averageWorkClass = 0
        #self.averageMaritialStatus = 0
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

    def calculateNumericAverages(self):
        self.averageAge = self.totalAge / self.count
        self.averageEducation = self.totalEducation / self.count
        self.averageCapitalGain = self.capitalGain / self.count
        self.averageCapitalLoss = self.capitalLoss / self.count
        self.averageHoursPerWeek = self.hoursPerWeek / self.count

    def calculateDiscreteAverages(self):
        self.averageWorkClass = {}
        for k,v in self.workClass.iteritems():
            self.averageWorkClass[k] = v / self.count

        self.averageMaritalStatus = {}
        for k,v in self.maritialStatus.iteritems():
            self.averageMaritalStatus[k] = v / self.count

        self.averageOccupation = {}
        for k,v in self.occupation.iteritems():
            self.averageOccupation[k] = v / self.count

        self.averageRelationship = {}
        for k,v in self.relationship.iteritems():
            self.averageRelationship[k] = v / self.count

        self.averageRace = {}
        for k,v in self.race.iteritems():
            self.averageRace[k] = v / self.count

        self.averageSex = {}
        for k,v in self.sex.iteritems():
            self.averageSex[k] = v / self.count

    def takeFeatures(self, line):
        self.incrementCount()
        self.assignDiscreteTotals(line)
        self.assignNumericTotals(line)
