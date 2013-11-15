import sys
import features

class CompareFeatures(object):
    def __init__(self, below50k, above50k):
        self.below50k = below50k
        self.above50k = above50k

    def Print(self):
        print self.below50k.title

    def Compare(self):
        print "compare"
