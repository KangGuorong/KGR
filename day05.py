#EP1
'''
class ep1:
    def __init__(self):
        self.num = 1000
    def check(self):
        if self.num % 2 == 0:
            print('ou')
        else:
            print('ji')
if __name__ == '__main__':
    ep1().check()
'''
#EP2
'''
class ep2:
    def __init__(self):
        self.num = 10
        print( 'init over!')
    def num2(self):
        self.num = self.num ** 2
        print self.num
    def num3(self):
        self.num = self.num ** 3
        print self.num
if __name__ == '__main__':
    kkk = ep2()
    kkk.num2()
    kkk.num3()
'''
#EP3

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        res = self.width * self.height
        print res
    def getPerimeter(self):
        res2 = 2 * (self.width + self.heightd)
        print res2
Rectangle(4,40).getArea()
Rectangle(4,40).getPerimeter()

