def factorial(a):
    FACT=1
    for i in range(1,a+1,1):
        FACT=FACT*i
    return FACT
n=input('enter a number')
fact=factorial(n)
print('the factorial of a number is {}'.format(fact))
