def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print("the fibo 5 is: ", fibo(5))
print("the fibo 7 is: ", fibo(7))
print("the fibo 6 is: ", fibo(6))