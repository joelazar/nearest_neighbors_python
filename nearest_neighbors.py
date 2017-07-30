#!/usr/bin/env python2
import sys
import time
import numpy
from sklearn.neighbors import NearestNeighbors

start = time.time()

try:
    param = sys.argv[1]
    my_array = numpy.loadtxt(param)
except IndexError:
    print "No param was given to the script - example usage: " \
          "./nearest_neighbors.py PATH_TO_TESTDATA"
    sys.exit(1)
except IOError:
    print "Wrong path to testdata given"
    sys.exit(1)

print my_array

nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(my_array)
distances, indices = nbrs.kneighbors(my_array)

solution = indices[numpy.argmin(numpy.delete(distances,0,1))]

print "%d:%s" % (solution[0]+1,' '.join(map(str,[int(floater) for floater in my_array[solution[0]]])))
print "%d:%s" % (solution[1]+1,' '.join(map(str,[int(floater) for floater in my_array[solution[1]]])))

end = time.time()
elapsed = end - start

print "Elapsed time : %.3f seconds" % elapsed
