#1
'''
import math
r = eval( raw_input ('Enter the length from the center to a vertex:'))
s = 2 * r * math.sin(math.pi / 5)
Area = 5 * s * s /(4 * ( math.tan(math.pi / 5)))
print('The area of the pentagon is {:.2f}'.format(Area))
'''
#2
'''
import math
x1,y1 = eval ( raw_input ('Enter point 1(latitude and longitude ) in degress:'))
x2,y2 = eval (raw_input ('Enter point 2(latitude and longitude ) in degress:'))
radius = 6371.0
s = math.sin(math.radians(x1)) * math.sin(math.radians(x2))
c = math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1)-math.radians(y2))
d = radius * math.acos(s + c )
print('The distance between the two points is {} km'.format(d))
'''
#3
'''
import math
s = eval (raw_input ('Enter the side:'))
Area = (5 * s * s ) / (4 * math.tan(math.pi / 5))
print('The area of the pentagon is {}'.format(Area))
'''
#4
'''
import math
n = eval (raw_input ('Enter the number of sides:'))
s = eval (raw_input ('Enter the side:'))
Area =( n * s * s) / ( 4 * (math.tan(math.pi / n)))
print('The area of the polygon is {:.14f}'.format(Area))
'''
#5
'''
import math
number = int (raw_input('Enter an ASCII code:'))
print('The character is {} '.format(chr(number)))
'''
#6
'''
name = raw_input('Enter employee\'s name :')
week = eval (raw_input('Enter number of hours worked in a week:'))
h = eval (raw_input('Enter hourly pay rate:'))
f = eval (raw_input('Enter hourly tax withholding rate:'))
s = eval (raw_input('Enter state tax withholding rate:'))
Gross = week * h
fw = Gross * f
sw = Gross * s
td = fw + sw
q = Gross - td
print('Employee Name:{}'.format(name))
print('Hours Worked:{}'.format(week))
print('Pay Rate:${}'.format(h))
print('Gross Pay:${}'.format(Gross))
print('Deductions:')
print('  Federal Withholding (20%):${}'.format(fw))
print('  State Withholding (9.0%):${:.2f}'.format(sw))
print('  Total Deduction:${:.2f}'.format(td))
print('Net Pay:${:.2f}'.format(q))
'''
#7
'''
number = int (raw_input('Enter an integer:'))
q = number // 1000
b = number % 1000 // 100
s = number % 100 // 10
g = number % 10
print(str(g) + str(s) + str(b) +  str(q) )
'''
#8
'''
yx = ''
for i in '1844948247@qq.com':
    yx = yx + chr (ord(i) + 1)
print(yx)
'''
#1
'''
import math
a,b,c = eval(raw_input('Enter a,b,c:'))
s = b * b - 4 * a *c
if s > 0:
    r1 = (-b + math.sqrt(b *b - 4 * a * c)) / 2 * a
    r2 = (-b - math.sqrt(b *b - 4 * a * c)) / 2 * a
    print('Tne roots are {:.6f} and {:.5f}'.format(r1,r2))
elif s == 0:
    r1 = (-b + math.sqrt(b *b - 4 * a * c)) / 2 * a
    r2 = (-b - math.sqrt(b *b - 4 * a * c)) / 2 * a
    r1=r2
    print('The root is {}'.format(r1))
if s < 0:
    print('The equation has no real roots')
'''
#2
'''
import random
n1 = random.randint(1,100)
n2 = random.randint(1,100)
print(n1)
print(n2)
num = n1 + n2
n = eval(raw_input('>>'))
if n==num:
    print('True')
else:
    print('false')
'''
#3
'''
today = eval (raw_input('Enter today\'s day:'))
days = eval (raw_input('Enter the number of days elapsed since taday:'))
week =( today + days) % 7
if week==0:
    print('Today is {} and the future day is Sunday '.format(today))
elif week==1:
    print('Today is {} and the future day is Monday '.format(today))
elif week==2:
    print('Today is {} and the future day is Tuesday '.format(today))
elif week==3:
    print('Today is {} and the future day is Wendnesday '.format(today))
elif week==4:
    print('Today is {} and the future day is Thursday'.format(today))
elif week==5:
    print('Today is {} and the future day is Firday'.format(today))
elif week==6:
    print('Today is {} and the future day is Sunday'.format(today))
'''
#4
'''
a,b,c= eval (raw_input('Enter a,b,c:'))
if a>b:
    a,b = b,a
if a>c:
    a,c = c,a
if b>c:
    b,c = c,b
print(a,b,c)
'''
#5
'''
w1,p1 = eval(raw_input('Enter weight and price for package 1:'))
w2,p2 = eval(raw_input('Enter weight and price for package 2:'))
b1 = p1 / w1
b2 = p2 / w2
if b1 < b2:
    print('Package 1 has the better price')
elif b1 > b2:
    print('Package 2 has the better price')
else:
    print('Package 1 the same as Package 2')
'''
#6
'''
y,m = eval (raw_input('Enter year and month:'))
if (y%400==0) | (y%4==0 & y%100!=0):
    if m==2:
        print('{}.{} have 29 days '.format(y,m))
    else:
        print('{}.{} have 28 days '.format(y,m))
else:
    if (m<=7 & m%2==1):
        print('{}.{} have 31 days '.format(y,m))
    else:
        print('{}.{} have 30 days '.format(y,m))
else:
    if m%2==1:
        print('{}.{} have 30 days '.format(y,m))
    else:
        print('{}.{} have 31 days '.format(y,m))
'''

#7
'''
import random
n = random.randint(0,1)
m = eval(raw_input('Enter a guess value(1 is front,0 is back )'))
if m==n:
    print('True')
else:
    print('False')
'''
#8

#10

#11
'''
n = eval (raw_input('Enter a three-digit integer:'))
b = n // 100
g = n % 10
if b==g:
    print('{} is a palindrome'.format(n))
else:
    print('{} is not a palindrome'.format(n))
'''
#12
a,b,c = eval(raw_input('Enter three edges:'))
C=a + b + c
if (a + b) > c:
    print('The perimeteris {}'.format(C))
else:
    print('illegal')
