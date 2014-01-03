from __future__ import division
from collections import defaultdict

AGE = 'Age' #0
WORKCLASS = 'Workclass' #1
EDUCATION_NUMBER = 'Education-number' #4
MARITAL_STATUS = 'Marital-status' #5
OCCUPATION = 'Occupation' #6
RELATIONSHIP = 'Relationship' #7
RACE = "Race" #8
SEX = "Sex" #9
CAPITAL_GAIN = 'Capital-gain' #10
CAPITAL_LOSS = 'Capital_loss' #11
HOURS_PER_WEEK = 'Hours-per-week' #12
RESULT = 'Result' #14

items = []

with open("sample.txt", 'rb') as f:
    for line in f:
        feature = line.split(',')
        dictLine = {}
        dictLine[AGE] = feature[0]
        dictLine[WORKCLASS] = feature[1]
        dictLine[EDUCATION_NUMBER] = feature[4]
        dictLine[MARITAL_STATUS] = feature[5]
        dictLine[OCCUPATION] = feature[6]
        dictLine[RELATIONSHIP] = feature[7]
        dictLine[RACE] = feature[8]
        dictLine[SEX] = feature[9]
        dictLine[CAPITAL_GAIN] = feature[10]
        dictLine[CAPITAL_LOSS] = feature[11]
        dictLine[HOURS_PER_WEEK] = feature[12]
        dictLine[RESULT] = feature[14]
        items.append(dictLine)

u50 = defaultdict(int)
u50Count = 0
o50Count = 0
for item in items:
    bracket = item[RESULT].rstrip()
    if (bracket == ' <=50K'):
        u50[AGE] += int(item[AGE])
        u50[EDUCATION_NUMBER] += int(item[EDUCATION_NUMBER])
        u50[HOURS_PER_WEEK] += int(item[HOURS_PER_WEEK])
        u50[CAPITAL_GAIN] += int(item[CAPITAL_GAIN])
        u50[CAPITAL_LOSS] += int(item[CAPITAL_LOSS])
        u50Count = u50Count + 1
    elif (bracket == ' >=50k'):
        o50Count = O50Count + 1

print u50[AGE]
print u50Count
print o50Count
