def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(4)
print(fact(n))