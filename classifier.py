from __future__ import division
from collections import defaultdict

import contextlib
import sys
import features

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

if __name__ == '__main__':
    main()
