#1
'''
def ssn(s):
    for i in s:
        if i>='0' and i<='9':
            print 'Valid SSN'

s=raw_input('ddd-dd-dddd:')
ssn(s)
'''

#2
'''
def fun(str1,str2):
    print str2.find(str1)
str1 = raw_input('Enter a string:')
str2 = raw_input('Enter a string:')
fun(str1,str2)
'''

#3
'''
def zifu(pwd):
    if len(pwd) >= 8:
        return  True
    else:
        return False
def ys(pwd):
    for i in range(len(pwd)):
        if (pwd[i]>='a' and pwd[i]<='z') or (pwd[i] >= 'A' and pwd[i] <= 'Z') or (pwd[i]>=0 and pwd[i]<=9):
            return True
        else:
            return False
def sum1(pwd):
    count = 0
    for i in range(len(pwd)):
        if pwd[i] >= 0 and pwd[i] <= 9:
            count +=1
    print count
    if count>=2:
        return True
    else:
        return False
def mima(pwd):
    if zifu(pwd) and ys(pwd) and sum1(pwd) == True:
        print 'valid password'
    else:
        print 'invalid password'
pwd = raw_input('Enter password:')
mima(pwd)
'''
#4
'''
def countLetters(s):
    sum1 = 0
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            sum1 +=1
    print sum1
s = raw_input('Enter a string:')
countLetters(s)
'''
#5
'''
def getNumber(num1):
    for i in range(len(num1)):
        if num1[i] >='0' and num1[i] <='9':
            print num1[i],
        elif (num1[i] >='a' and num1[i] <= 'c') or (num1[i] >='A' and num1[i] <= 'C'):
            print 2,
        elif (num1[i] >='d' and num1[i] <= 'f') or (num1[i] >='D' and num1[i] <= 'F'):
            print 3,
        elif (num1[i] >='g' and num1[i] <= 'i') or (num1[i] >='G' and num1[i] <= 'I'):
            print 4,
        elif (num1[i] >='j' and num1[i] <= 'l') or (num1[i] >='J' and num1[i] <= 'L'):
            print 5,
        elif (num1[i] >='m' and num1[i] <= 'o') or (num1[i] >='M' and num1[i] <= 'O'):
            print 6,
        elif (num1[i] >='p' and num1[i] <= 's') or (num1[i] >='P' and num1[i] <= 'S'):
            print 7,
        elif (num1[i] >='t' and num1[i] <= 'y') or (num1[i] >='T' and num1[i] <= 'Y'):
            print 8,
        elif (num1[i] >='w' and num1[i] <= 'z') or (num1[i] >='W' and num1[i] <= 'Z'):
            print 9,
num1 = raw_input('Enter phone number:')
getNumber(num1)
'''
#6
'''
def reverse(s):
    s1 = list(s)
    s1.reverse()
    print ''.join(s1)
s = raw_input('Enter a string:')
reverse(s)
'''
#7
'''
def checkCard(card_num):
    card_list = list(card_num)   #zhuanwei list
    Res = 0
    Res2 = 0
    for i in range(len(card_list)):
        res = int(card_list[i]) * 2
        if  res >= 10:
            res1 = res % 10  # ge wei
            res2 = res // 10 # shi wei
            res3 = res2 +res1
            Res += res3
        else:
            Res += res
        if i % 2 != 0:
            Res2 += int(card_list[i])
    RES = Res + Res2
    if RES % 10 ==0:
        print('hefa')
    else:
        print('buhefa')
card_num = '438857601840707'
checkCard(card_num)

'''

#8
'''
def checkISBN(str_):
    str_list = list(str_)
    sum1 = 0
    for i in range (len(str_list)):
        if i % 2 ==0:
            res = int(str_list[i]) * 3
        else:
            res = int(str_list[i])
        sum1 += res
    RES = 10 -sum1 % 10
    if RES == 10:
        RES = 0
    print(RSE)
str_ = input('>>')
checkISBN(str_)
'''
