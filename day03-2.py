#1
'''
n = -1
z,f,sum1 = 0,0,0
while n != 0:
    n = eval(raw_input('Enter an integer,the input ends if it is 0:'))
    if n > 0:
        z += 1
    if n < 0:
        f +=1
    sum1 += n
p = float(sum1 )/ (z + f)
print('positive number is: {}'.format(z))
print('negative number is: {}'.format(f))
print('sum is: {}'.format(sum1))
print('average is {}'.format(p))
'''
#2
'''
money = 10000
money1 = 10000
i=0
while i<10:
    money += money * 0.05
    i +=1
    money1 +=money
print(money,money1)
'''
#4
'''
n=0
for i in range(100,1001):
    if (i%5==0) & (i%6==0):
        print(i,' ',end='')
        n +=1
    if n == 10:
        print('\n')
        n=0
'''
'''
n=100
m=0
while n<=1000:
    n +=1
    m +=1
    if (n%5==0) & (n%6==0):
        print(n)
    if m%10==0:
    print('\n')
'''
#5
'''
n = 1;
while ( n*n<12000):
    n +=1
print(n)
'''
'''
n1 = 12000
while ( n1*n1*n1>12000):
    n1 -=1
print(n1)
'''
#6
'''
l = 0.05
d = eval(input("Loan Amount:"))
t = eval(input("Number of Years:"))
f1 = d * pow( 1+l,t)
f2=f1 / (12*t)
print('Interest Rate    Monthly Payment     Total Payment')
print("%.5f     	%.2f                %.2f"%(l,f2,f1))
'''


#7
'''
z = 50001
num = 0
for i in range (1,50001):
    m = 1 /(z-i)
    num +=m
print(num)
'''
#8
'''
a = 1
b = 3
n = 1 / 3
while( a<97 ):
	a += 2
	b += 2
	n += a/b
print(n)
'''
#9
'''
a = eval(input())
sum1 = 0
for i in range(1,a+1):
    sum1 +=pow((-1),(i+1)) / (2 * i -1)
pi = 4 * sum1
print(pi)
'''
#10
'''
for i in range(1,10001):
    s = 0
    for j in range(1,):

'''
#11
'''
sum1=0
for i in range(1,8):
	for j in range(i+1,8):
		print(i,' ',j)
		sum1 +=1
print(sum1)
'''
