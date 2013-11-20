import sys
from collections import defaultdict

class RecordAttributes(object):
    def __init__(self):
        self.workClass = defaultdict(int)
        self.maritialStatus = defaultdict(int)
        self.occupation = defaultdict(int)
        self.relationship = defaultdict(int)
        self.race = defaultdict(int)
        self.sex = defaultdict(int)

        self.averageAge = 0
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


