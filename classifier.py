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

    below50k.calculateNumericAverages()
    below50k.calculateDiscreteAverages()
    above50k.calculateNumericAverages()
    above50k.calculateDiscreteAverages()

    comparer = compare.CompareFeatures(below50k, above50k)
    comparer.Print()
    comparer.Compare()

    print comparer.average
    print comparer.averageEducation

if __name__ == '__main__':
    main()
