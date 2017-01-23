#http://matplotlib.org/api/pyplot_summary.html

#C:\Users\user\AppData\Local\Programs\Python\Python35\Scripts>

#pip3.exe install matplotlib

#import matplotlib

import turtle

import math

class Dot(object):

    def __init__(self, x=0, y=0):

        self.x = x

        self.y = y

    def dot_coord(self):

        print ('X={x},Y={y}'.format(x = self.x,y = self.y))

    def dot_add(self):

        print('dot_add')

    def __str__(self):

        return ('point x={x},y={y}'.format(x = self.x,y = self.y))

    def __add__(self,other):

        return Dot(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):

        self.x += other.x

        self.y += other.y

        return self

    def move(self, x=0, y=0):

        #print ('Point moove (x {}) (y {})'.format(x, y))

        self.x = self.x + x

        self.y = self.y + y

        #print ('Point mooved to (x {}) (y {})'.format(self.x, self.y))

        return self



#=Dot(1,5)

#a.dot_coord()





class Fig(object):

    def square(self):

        raise NotImplementedError

    def __str__(self):

        return 'figure with no specifications'

class Circle(Fig):

    LABEL='Circle'

    def __init__(self, a=(0,0), r=0):

        self.a=a

        self.radius = r

        print ('Circle create:\nCentral point at {}\nRadius = {}'.format(self.a,self.radius))

    def square(self):

        return math.pi * self.radius ** 2

    def __str__(self):

        return 'Circle. Center in {} R={}'.format(self.a,self.radius)

    def rad(self):

        return 'Radius = {}'.format(self.radius)

    def move(self, x=0, y=0):

        print ('Point moove (x {}) (y {})'.format(x,y))

        self.x = x

        self.y = y

        self.a.move(x, y)

        return self

class Rect(Fig):

    LABEL = 'Rect'

    def __init__(self, a=(0,0), b=(0,0), c=(0,0), d=(0,0)):

        self.a = a

        self.b = b

        self.c = c

        self.d = d

        self.width = self.d.x- self.a.x

        self.height = self.b.y- self.a.y

        print('Rect Create : \nA at {}, \nB at {}, \nC at {}, \nD at {}'.format(self.a, self.b, self.c, self.d))

    def square(self):

        return self.width * self.height

    def __str__(self):

        return 'Rect: \nA at {},\nB at {},\nC at {},\nD at {}\nRect Width = {}\nRect Height = {}'.format(self.a, self.b, self.c, self.d, self.width, self.height)

    def move(self, x=0, y=0):

        print ('Point moove (x {}) (y {})'.format(x, y))

        self.a.move(x,y)

        self.b.move(x,y)

        self.c.move(x,y)

        self.d.move(x,y)

        return self

class Square(Rect):

    LABEL = 'Square'

    def __init__(self, x):

        super().__init__(x, x)

    def square(self, verbose=False):

        s = super().square()

        if verbose:

            print('square square = {}'.format(s))

        return s





a=Dot(1,1)

b=Dot(1,2)

c=Dot(3,2)

d=Dot(3,1)

c1=Dot(1,1)



k=Circle(c1,1)

k.move(5,5)

print(k)

print (k.square())

print (k.rad())

k.radius=11

print (k.rad())

print (k.square())



s=Rect(a,b,c,d)

s.move(5,5)

print(s)

turtle.circle(45)
