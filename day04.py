#1
'''
def getPentagonalNumber(n):
    c = 0
    for i in range(1,n+1):
        m = i * ( 3 * i -1) / 2
        print(m,'',end='')
        c +=1
        if c%10== 0:
            print('\n')
getPentagonalNumber(100)
'''
#2
'''
def sumDigits(n):
    sum1=0
    while(n%10!=0):
        a = n%10
        sum1 += a
        n = n//10
    print(sum1)
n = eval(input('Enter an integer:'))
sumDigits(n)
'''

#3
'''
def displaySortedNumbers(num1,num2,num3):
    if num1>num2:
        num1,num2 = num2,num1
    if num1>num3:
        num1,num3 = num3,num1
    if num2>num3:
        num2,num3 = num3,num2
    print('The sorted numbers are{} {} {}'.format(num1,num2,num3))
n1,n2,n3 = eval(input('Enter three numbers:'))
displaySortedNumbers(n1,n2,n3)
'''
#4
'''
investmentAmount = eval(input('The amount invested:'))
monthlyInterestRate = eval(input('Annual interest rate:'))
def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
    return investmentAmount*pow((1+monthlyInterestRate/100/12),years*12)
for years in range(1,31):
    num=futureInvestmentValue(investmentAmount,monthlyInterestRate,years)
    print("%d\t%.2f"%(years,num),end="  ")
    print()
'''
#5
'''
def printChars(ch1,ch2,numberPerLine):
    s = 0
    a = ord(ch1)
    b = ord(ch2)+1
    for i in range(a,b):
        print(chr(i),end=' ')
        s = s + 1
        if(s % numberPerLine==0):
            print(' ')
printChars('1','Z',10)
'''
#6
'''
def numberOfDaysInYear(year):
    for i in range(year,2021):
        if((year%400==0)|(year%4==0)&(year%100!=0)):
            print('{} is 366'.format(year))
        else:
            print('{} is 365'.format(year))
        year +=1
numberOfDaysInYear(2010)
'''
#7
'''
def distance(x1,y1,x2,y2):
    print(((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))*0.5)
x1,y1=eval(input('Enter x1 and y1:'))
x2,y2=eval(input('Enter x2 and y2:'))
distance(x1,y1,x2,y2)
'''
#8

#9
'''
from time import *
print(ctime(time()))
'''
#10
'''
a,b=eval(input('>>'))
if(a+b==2)|(a+b==3)|(a+b==12):
    print('You rooled{}+{}={}'.format(a,b,a+b))
    print('You lose')
elif(a+b==7)|(a+b==11):
    print('You rooled{}+{}={}'.format(a,b,a+b))
    print('You win')
else:
    while(1):
        print('You rooled{}+{}={}'.format(a,b,a+b))
        print('print is {}'.format(a+b))
        sum1=a+b
        a,b=eval(input('>>'))
        if(a+b==7):
            print('You rooled{}+{}={}'.format(a,b,a+b))
            print('You lose')
            break
        elif(a+b==sum1):
            print('You rooled{}+{}={}'.format(a,b,a+b))
            print('You win')
            break
        else:
            continue
'''





