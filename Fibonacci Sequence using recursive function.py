#Fibonacci sequence using recursive function.
def fib(n):
    if n<=0:
        return f'Incorrect input.'
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input('Enter which fibonacci number you want:'))
print(f'{n}th element in fibonacci seq. is: {fib(n)}')
print(f'\nEntire Fibonacci Sequence is:')
for i in range(1,n+1):
    print(fib(i), end=' ')

