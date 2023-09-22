def sumofevenfibonacci(N):
    a, b = 1, 2
    even_sum = 0

    while a <= N:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum

T = int(input())

for _ in range(T):
    N = int(input())
    result = sumofevenfibonacci(N)
    print(result)
