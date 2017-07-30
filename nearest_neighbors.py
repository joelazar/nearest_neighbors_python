#!/usr/bin/env python2
import sys
import time
import numpy
from sklearn.neighbors import NearestNeighbors


class InputData:
    def __init__(self, inputfile):
        try:
            self.array = numpy.loadtxt(inputfile)
            self.solution = None
            #print self.array
        except IOError:
            print "Wrong path to testdata given"
            sys.exit(1)

    def findNearestNeighbors(self):
        nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(self.array)
        (distances, indices) = nbrs.kneighbors(self.array)
        self.solution = indices[numpy.argmin(numpy.delete(distances,0,1))]

    def logSolution(self):
        print "%d:%s" % (self.solution[0]+1,'\t'.join(map(str,[int(round(floater)) for floater in self.array[self.solution[0]]])))
        print "%d:%s" % (self.solution[1]+1,'\t'.join(map(str,[int(round(floater)) for floater in self.array[self.solution[1]]])))

def nearest_neighbors(inputfile):

    data = InputData(inputfile)
    data.findNearestNeighbors()
    data.logSolution()

if __name__ == '__main__':
    try:
        start = time.time()
        nearest_neighbors(sys.argv[1])
        end = time.time()
        elapsed = end - start
        print "Elapsed time : %.3f seconds" % elapsed
    except IndexError:
        print "No param was given to the script - example usage: " \
            "./nearest_neighbors.py PATH_TO_TESTDATA"
        sys.exit(1)