def fac_fib(n):
    # calculate factirial
    fact = n
    if n == 0:
        fact = 1
    else:
        for i in range(1,n):
            fact *= i
    
    #calculate fibonacci
    a = 0; b = 1
    for i in range(3,n+1):
        a,b = b,a+b
    
    return (fact,b)

n = int(input('number: '))
result = fac_fib(n)
print("factorial of",n,"=",'{} and fibonacci = {}'.format(result[0],result[1]))