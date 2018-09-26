'''import math
x1,y1 = eval (raw_input(">>"))
x2,y2 = eval (raw_input(">>"))
x3,y3 = eval (raw_input(">>"))
a=math.sqrt(math.pow((x2-x3),2)+math.pow((y2-y3),2))
b=math.sqrt(math.pow((x1-x3),2)+math.pow((y1-y3),2))
c=math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
A=math.degrees(math.acos((a*a-b*b-c*c) / (-2 * b * c )))
B=math.degrees(math.acos((b*b-a*a-c*c) / (-2 * a * c )))
C=math.degrees(math.acos((c*c-b*b-a*a) / (-2 * a * b )))
print(A,B,C)
'''
#print('Welcome '+'to '+'python')

'''
n = eval (raw_input(">>"))
if int(n%2) == 0:
    print("oushu")
else:
    print("jishu")
'''
'''
print('start')
n = raw_input('')
if n == 'y':
    n2 = raw_input('')
    if n2 == 'y':
        n3 = raw_input('')
        if n3 == 'f':
            n4 = raw_input('')
            if n4 == 'y':
                print('jj')
            else:
                print('mfq')
        else:
            print('g')
    else:
        print('k')
else:
    print('g')
'''
import random
n = random.randint(1,10)
number = eval ( raw_input(''))
if number > n:
    print('dale')
elif number < n:
    print(xiaole)
else:
    print('duile')






