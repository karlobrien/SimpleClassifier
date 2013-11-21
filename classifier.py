from __future__ import division

import features
import compare

def main():
    below50k = features.Features("below50k")
    above50k = features.Features("above50k")

    with open("sample.txt", 'rb') as f:
        for line in f:
            feature = line.split(',')
            outcome =  feature[14].rstrip()
            if (outcome == ' <=50K'):
                below50k.takeFeatures(feature)
            if (outcome == ' >50K'):
                above50k.takeFeatures(feature)

    print below50k.title

    below50k.calculateNumericAverages()
    below50k.calculateDiscreteAverages()

    print below50k.averageRace

    above50k.calculateNumericAverages()
    above50k.calculateDiscreteAverages()

    print above50k.averageRace
    comparer = compare.CompareFeatures(below50k, above50k)
    comparer.Print()
    comparer.Compare()

    print comparer.average
    print comparer.averageEducation

if __name__ == '__main__':
    main()
