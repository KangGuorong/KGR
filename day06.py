#1
'''
url = 'http://www.baidu.com/?page=?wd=red'

for i in range(100):
    part1 = 'http://www.baidu.com/?page='
    res = part1 + str(i) + '?wd=red'
    print res
    i +=1
'''
#2
'''
A2 = [1,1,1,1,1,1,2,2,2,2,3]
a2 = []
for i in A2:
    if i not in a2:
        a2.append(i)
print a2
'''
#3
'''
a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
a4.sort(key=lambda x:x[1])
print a4
'''
'''
a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
a5 = sorted(a4,key=lambda x:x[2][1])
print a4
print a5
'''
#pop
'''
A5 = [1,2,3,'a',True]
pop_ele = A5.pop(0)
print A5
'''

#spilt
'''
a = 'a,b,c,d'
b = 'a b c d'
print a.split(',')
print b.split(' ')
'''

#
