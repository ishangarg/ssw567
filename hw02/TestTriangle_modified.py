# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle_modified import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(int(3),int(4), int(5)),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testNotTriangle(self): 
        self.assertEqual(classifyTriangle(2,2,5),'NotATriangle','2, 2, 5 is not a tirangle')
    
    def testIsosceles(self):
        self.assertEqual(classifyTriangle(6,6,5),'Isoceles','6, 6, 5 is a isosceles')
        self.assertEqual(classifyTriangle(5,6,5),'Isoceles','5, 6, 5 is a isosceles')


    def testUpperBound(self):
        self.assertEqual(classifyTriangle(600,6,5),'InvalidInput','600, 6, 5 is an invalid input')

    def testLowerBound(self):
        self.assertEqual(classifyTriangle(2,0,5),'InvalidInput','2, 0, 5 is an invalid input')

    def testFloat(self):
        self.assertEqual(classifyTriangle(0.1,0.5,1.0),'InvalidInput','0.1,0.5,1.0 is an invalid input')





if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

