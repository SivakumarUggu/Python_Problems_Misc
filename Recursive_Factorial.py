#Factorial of a given number using recursive method.
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input('Enter any number:'))
print(f'Factorial of {n} is:', fact(n))