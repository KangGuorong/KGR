#1
'''
def score(cj):
    for i in range(len(cj)):
        if int(cj[i]) >= int(max(cj)) - 10:
            print('Student {} score is {} and grade is A'.format(i,cj[i]))
        elif int(cj[i]) >= int(max(cj)) - 20:
            print('Student {} score is {} and grade is B'.format(i,cj[i]))
        elif int(cj[i]) >= int(max(cj)) - 30:
            print('Student {} score is {} and grade is C'.format(i,cj[i]))
        elif int(cj[i]) >= int(max(cj)) - 40:
            print('Student {} score is {} and grade is D'.format(i,cj[i]))
        else:
            print('Student {} score is {} and grade is F'.format(i,cj[i]))
cj= raw_input('Enter scores:')
c = cj.split(' ')
score(c)
'''

#2
'''
def list1(a):
    a.reverse()
    print a
a = input('Enter a list:')
list1(a)
'''
#3
'''
def integers(n):
    n1 = set(n)
    for i in n1:
        print('{} occurs {} times'.format(i,n.count(i)))
n = raw_input('')
m = n.split()
integers(m)
'''
#4
'''
def fun(n):
    sumf,sumg,d,x,ave=0,0,0,0,0
    for i in n:
        sumf +=float(i)
        sumg +=1
    ave = sumf / sumg
    for i in range(len(n)):
        if float(n[i])>=ave:
            d +=1
        else:
            x +=1
    print('Scores greater than the average score are:{}'.format(d))
    print('Scores less than the average score are:{}'.format(x))
n = raw_input('Enter score:')
n1 = n.split()
fun(n1)
'''
#5
'''
import random
def ran(n):
    n1 = set(n)
    for i in n1:
        print('{} occurs {} times'.format(i,n.count(i)))
n = [random.randint(0,9) for i in range (1000)]
ran(n)     
'''
#6
'''
def index(lst):
    l = min(lst)
    s = str(lst)
    a = s.find(l)
    print a
lst = raw_input('>>')
lst1 = lst.split(' ')
index(lst)
'''
#7
'''
import random
def shuffle(lst):
    lst1 = list(lst)
    random.shuffle(lst1)
    print lst1
lst = raw_input('>>')
l = lst.split(',')
shuffle(l)
'''
#8
'''
def eliminateDuplicates(lst):
    for i in A2:
        if i not in a2:
            a2.append(i)
    print('The distinct numbers are:{}'.format(a2))
a2 = []
A2 = input('Enter ten numbers:')
eliminateDuplicates(A2)
'''
#8
'''
def eliminateDuplicates(lst):
    lst1 = set(lst)
    print list(lst1)
lst = input('Enter ten numbers:')
eliminateDuplicates(lst)
'''
#9
'''
def isSorted(ls):
    lst1 = sorted(ls)
    lst = list(ls)
    if lst == lst1:
        print('The list is already sorted')
    else:
        print('The list is not sorted')
ls = raw_input('Enter list:')
l = ls.split(' ')
isSorted(l)
'''
#10
'''
def fun(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    print lst
lst = raw_input('Enter ten numbers:')
l = lst.split(' ')
fun(l)
'''
#11
'''
import random
def youhuiquan():
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    list2 = ['h','t','m','f']
    list3 = []
    count = 0
    while len(list3) !=4:
        count +=1
        r1 = random.randint(0,12)
        r2 = random.randint(0,3)
        if list2[r2] not in list3:
            print('huo de pai : {} {}'.format(list2[r2],list1[r1]))
            list3.append(list2[r2])
    print('Pick:' + str(count))
youhuiquan()

'''

#12
'''
def isConsecutveFour(values):
    list1 = list(str(values))
    if len(list1) >= 4:
        for i in range(len(list1)-3):
            if list1[i] == list1[i+1] and list1[i] == list1[i+2] and list1[i] == list1[i+3]:
                print('you')
                break
            else:
                print('meiyou')
                break
    else:
        print('shibei')
values = raw_input('>>')
isConsecutveFour(values)
'''
