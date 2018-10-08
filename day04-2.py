#2
def sumDigits(n):
    while(n>0):
        sum1 = 0
        if n<10:
            return n
        else:
            sum1 += n%10
            n /=10
            return sum1
main():
    sum1 = 0
    n = eval(input('Enter an integer:'))
    sum1 = sumDigits(n)
    print(sum1)
