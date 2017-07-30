#!/usr/bin/env python2
from nearest_neighbors import nearest_neighbors

from cStringIO import StringIO
import sys
import unittest

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

class TestStringMethods(unittest.TestCase):

    def base_test(self, inputfile, outputfile):
        with Capturing() as output:
            nearest_neighbors(inputfile)
        f = open(outputfile, 'r')
        i = 0
        for line in f:
            self.assertEqual(line.strip(), output[i])
            i = i+1

    def test_sample_input_2_8(self):
        self.base_test("testdata/sample_input_2_8.tsv", "testdata/sample_output_2_8.txt")

if __name__ == '__main__':
    unittest.main()
