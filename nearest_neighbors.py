#!/usr/bin/env python2
import sys
import time
import numpy
from sklearn.neighbors import NearestNeighbors


class InputData(object):
    def __init__(self, inputfile):
        try:
            self.array = numpy.loadtxt(inputfile)
            self.solution = None
        except IOError:
            print "Wrong path to testdata given"
            sys.exit(1)

    def find_nearest_neighbors(self):
        nbrs = NearestNeighbors(n_neighbors=2, algorithm='auto').fit(self.array)
        (distances, indices) = nbrs.kneighbors(self.array)
        self.solution = indices[numpy.argmin(numpy.delete(distances, 0, 1))]

    def log_solution(self):
        print "%d:%s" % (self.solution[0]+1,
                         '\t'.join(map(str,[int(round(flt)) for flt in self.array[self.solution[0]]])))
        print "%d:%s" % (self.solution[1]+1,
                         '\t'.join(map(str,[int(round(flt)) for flt in self.array[self.solution[1]]])))

def nearest_neighbors(inputfile):

    data = InputData(inputfile)
    data.find_nearest_neighbors()
    data.log_solution()

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
