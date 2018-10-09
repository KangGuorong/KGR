#1
'''
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        res = self.width * self.height
        print res
    def getPerimeter(self):
        res2 = 2 * (self.width + self.height)
        print res2
Rectangle(4,40).getArea()
Rectangle(4,40).getPerimeter()
'''
#2
'''
class Account:
    def __init__(self,id1,balance,annualInterestRate):
        self.__id1 = id1
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    def getMonthlyInterestRate(self):
        yll = self.__annualInterestRate / 12
        print yll
    def getMonthlyInterest(self):
        ylx = self.__balance * (self.__annualInterestRate / 100 / 12)
        print ylx
        return ylx
    def withdraw(self):
        self.__balance = self.__balance - 2500
        yll = self.__annualInterestRate / 12
        ylx = self.__balance * (self.__annualInterestRate / 100 / 12)
        print self.__balance , yll ,ylx
    def deposit(self):
        self.__balance = self.__balance + 3000
        yll = self.__annualInterestRate / 12
        ylx = self.__balance * (self.__annualInterestRate / 100 / 12)
        print self.__balance,yll,ylx
#Account('1122',20000,4.5).getMonthlyInterestRate()
#Account('1122',20000,4.5).getMonthlyInterest()
Account('1122',20000,4.5).withdraw()
Account('1122',20000,4.5).deposit()
'''
#3
'''
import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    def getPerimeter(self):
        zc = self.__side * self.__n
        print zc
    def getArea(self):
        mj = (self.__n * ( self.__side ** 2) ) / (4 * math.tan(math.pi/self.__n))
        print mj
if __name__ == '__main__':
    R1 = RegularPolygon()
    R2 = RegularPolygon(6,4)
    R3 = RegularPolygon(10,4,5.6,7.8)
    R1.getPerimeter()
    R1.getArea()
    R2.getPerimeter()
    R2.getArea()
    R3.getPerimeter()
    R3.getArea()
'''
#4
'''
class Fan:
    def __init__(self,speed=1,on=False,radius=5,color='blue'):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    def show(self):
        print self.__speed,self.__on,self.__radius,self.__color
F1 = Fan()
F2 = Fan(3,True,10,'yellow')
F3 = Fan(2,False,5,'blue')
F1.show()
F2.show()
F3.show()
'''
#5
'''
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def isSolvable(self):
        if self.__a * self.__d - self.__b * self.__c != 0:
            print 'true'
        else:
            print 'The equation has no solution'
    def getX(self):
        x = (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        print x
    def getY(self):
        y = (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        print y  
a,b,c,d,e,f = eval (raw_input('>>'))
LE=LinearEquation(a,b,c,d,e,f)
LE.isSolvable()
LE.getX()
LE.getY()
'''
#6

class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def isSolvable(self):
        if self.__a * self.__d - self.__b * self.__c != 0:
            print 'true'
        else:
            print 'The equation has no solution'
    def getX(self):
        x = (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        print x
    def getY(self):
        y = (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        print y  
x1,y1,x2,y2 = eval(raw_input('Enter the endpoints of the first line segment:'))
x3,y3,x4,y4 = eval(raw_input('Enter the endpoints of the second line segment:'))



LE=LinearEquation()
LE.isSolvable()
       
