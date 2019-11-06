import unittest
from tests.TestClass1 import TestClass1
from tests.TestClass2 import TestClass2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2])

import argparse
# create a new argument parser
parser = argparse.ArgumentParser(description="Simple argument parser")
# add a new command line option, call it '-c' and set its destination to 'config'
#parser.add_argument("-c", action="store", dest="config_file")
parser.add_argument('-b', action='store', dest='browser',
                    help='Browser Value')
parser.add_argument('-p', action='store', dest='platform',
                    help='Operating System (MAC/WINDOWS)')

# get the result
result = parser.parse_args()
# since we set 'config_file' as destination for the argument -c,
# we can fetch its value like this (and print it, for example):
#print(result.config_file)

for test in smokeTest:

    test.setUp(result.browser, result.platform)

unittest.TextTestRunner(verbosity=2).run(smokeTest)