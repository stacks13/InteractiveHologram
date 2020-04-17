# Something like this probably already existed but I made this all the same
import numpy as np
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, pt2):
        if type(pt2) == Point:
            return Point(self.x + pt2.x, self.y + pt2.y)

    def __sub__(self, pt2):
        if type(pt2) == Point:
            return Point(self.x - pt2.x, self.y - pt2.y)
        
    def __mul__(self, a):
        return Point(self.x*a, self.y*a)
    
    def __truediv__(self, a):
        return Point(self.x/a, self.y/a)
    
    def __repr__(self):
        return "(x: {}, y: {})".format(self.x, self.y)
    
    def copy(self):
        return Point(self.x, self.y)
    
    def ls(self):
        return [self.x, self.y]
    
    def d(self):
        return {'x': self.x, 'y': self.y}
    
    @staticmethod
    def avg(pts):
        temp = Point(0, 0)
        for i in pts:
            if i is not None:
                temp += i
        temp = temp / max(len(pts), 1)
        return temp
    
    @staticmethod
    def dist(a, b):
        return round(math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2))

    @staticmethod
    def conv_np(pts):
        return np.array([i.ls() for i in pts])