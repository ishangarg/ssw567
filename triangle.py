
import unittest

class Triangle():

    RIGHT = ""
    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"

    CLASSIFICATION = ""

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

        if not self.is_triangle():
            raise Exception("Not A Triangle")
        
    # def set_up_triangle(self, a, b, c):
        
    def classify(self) -> str:
        if self.is_equilateral():
            self.CLASSIFICATION = self.EQUILATERAL
        elif self.is_isosceles():
            self.CLASSIFICATION = self.ISOSCELES
        elif self.is_scalene():
            self.CLASSIFICATION = self.SCALENE
        
        if self.is_right():
            self.RIGHT = "and right"
        else:
            self.RIGHT = "and not right"

        return "%s %s" % (self.CLASSIFICATION, self.RIGHT)

    def is_triangle(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return True
        return False
    
    def is_equilateral(self):
        return self.a == self.b == self.c
    
    def is_isosceles(self):
        if self.a == self.b or self.b == self.c or self.a == self.c : 
            return True
        return False
    
    def is_scalene(self):
        if not self.a == self.b == self.c:
            return True
        return False
    
    def is_right(self):
        return (self.a ** 2 + self.b **2 == int(self.c ** 2)) or (self.b ** 2 + self.c **2 == int(self.a ** 2)) or (self.a ** 2 + self.c **2 == int(self.b ** 2))
    

class TriangleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.INPUT = {}
        self.INPUT['equilateral'] = {'not_right':{'pass':[2,2,2], 'fail':[2,3,4]}, 'right':{}}
        self.INPUT['scalene'] = {'not_right':{'pass':[2,3,4], 'fail':[2,2,2]}, 'right':{'pass':[3,4,5], 'fail':[2,2,2]}}
        self.INPUT['isosceles'] = {'not_right':{'pass':[2,2,4], 'fail':[2,2,2]}, 'right':{'pass':[5,5,7.07106781187], 'fail':[2,3,4]}}
        self.INPUT['not_triangle'] = [2, 1, 8]

    def test_equilateral_pass(self):
        points = self.INPUT['equilateral']['not_right']['pass']
        t = Triangle(points[0], points[1], points[2])
        s = t.classify()
        self.assertEqual(s, 'equilateral and not right')

    def test_equilateral_fail(self):
        points = self.INPUT['equilateral']['not_right']['fail']
        t = Triangle(points[0], points[1], points[2])
        #  t.is_equilateral()
        self.assertFalse(t.is_equilateral())
    
    # def test_wrong_equilateral_notright_fail(self): #funciton to check if assetion fails
    #     points = self.INPUT['equilateral']['not_right']['fail']
    #     t = Triangle(points[0], points[1], points[2])
    #     self.assertTrue(t.is_equilateral())

    def test_scalene_pass(self):
        point_right = self.INPUT['scalene']['right']['pass']
        point_not_right = self.INPUT['scalene']['not_right']['pass']

        t = Triangle(point_right[0], point_right[1], point_right[2])
        self.assertEqual(t.classify(), 'scalene and right')

        t = Triangle(point_not_right[0], point_not_right[1], point_not_right[2])
        self.assertEqual(t.classify(), 'scalene and not right')


    def test_scalene_fail(self):
        point_right = self.INPUT['scalene']['right']['fail']
        point_not_right = self.INPUT['scalene']['not_right']['fail']

        t = Triangle(point_right[0], point_right[1], point_right[2])
        self.assertFalse(t.is_scalene())

        t = Triangle(point_not_right[0], point_not_right[1], point_not_right[2])
        self.assertFalse(t.is_scalene())

    def test_triangle(self):
        points = self.INPUT['not_triangle']
        # try:
        with self.assertRaises(Exception):
            t = Triangle(points[0],points[1], points[2])

    def test_isosceles_pass(self):
        point_right = self.INPUT['isosceles']['right']['pass']
        t = Triangle(point_right[0], point_right[1], point_right[2])

        self.assertEqual(t.classify(), 'isosceles and right')

    def test_isosceles_fail(self):
        point_right = self.INPUT['isosceles']['right']['fail']
        t = Triangle(point_right[0], point_right[1], point_right[2])
        self.assertFalse(t.is_isosceles())




if __name__ == '__main__':
    unittest.main()