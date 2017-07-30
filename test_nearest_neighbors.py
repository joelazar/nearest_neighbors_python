#!/usr/bin/env python2
from cStringIO import StringIO
import sys
import unittest

from nearest_neighbors import nearest_neighbors

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

    def test_sample_input_3_1000(self):
        self.base_test("testdata/sample_input_3_1000.tsv", "testdata/sample_output_3_1000.txt")

    def test_sample_input_4_4(self):
        self.base_test("testdata/sample_input_4_4.tsv", "testdata/sample_output_4_4.txt")

    def test_sample_input_10_100(self):
        self.base_test("testdata/sample_input_10_100.tsv", "testdata/sample_output_10_100.txt")

    def test_sample_input_100_100(self):
        self.base_test("testdata/sample_input_100_100.tsv", "testdata/sample_output_100_100.txt")

if __name__ == '__main__':
    unittest.main()
