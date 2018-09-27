'''
for i in 'asdf':
    print(i)

a = 'asdfg'
i = 0
while i<5:
    print(a[i])
    i +=1
'''
'''
import random
n = random.randint(1,5)
m = eval (raw_input('>>'))
if n == m:
    print('GOOD')
else:
    while m != n:
        m = eval (raw_input('>>'))
        if m==n:
            print('true')
        else:
            print('Eoor')

    
'''
'''
import random
n = random.randint(1,5)
while 1:
'''
#EP2
'''
sum1 = 0
i = 0
while i<1001:
    sum1 = sum1 + i
    i +=1
'''
#EP3
'''
sum1 = 0
for i in range(10000):
    sum1 = sum1 + i
    if sum1 > 10000:
        break
print(sum1)
'''
#EP4
'''
for i in range(1,10):
    for j in range(1,i + 1):
        s = i * j
        print('{} x {} = {}'.format(i,j,s))
    print(' ' )
'''
#5
'''
def fun1(n1,n2):
    pass
    return n1,n2
def fun2(n1,n2):
    m1 = n1 ** 2
    m2 = n2 ** 2
    return m1,m2
def fun3(n1,n2,n3,n4):
    res1 = n3 - n1
    res2 = n4 - n2
    print(res1,res2)
a,b=fun1(1,2)
c,d=fun2(a,b)
fun3(a,b,c,d)
