def Fibonacci_digui(n):
    if n<=1:
        return 1
    else:
        return (Fibonacci_digui(n-1)+Fibonacci_digui(n-2))
print(list(Fibonacci_digui(8)))
# for i in range(8):
#     print(Fibonacci_digui(i))
