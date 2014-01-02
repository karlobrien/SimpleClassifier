from __future__ import division

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

items = []


with open("sample.txt", 'rb') as f:
    for line in f:
        feature = line.split(',')
        print feature[0]
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

        items.append(dictLine)

print items

