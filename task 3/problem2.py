def simplearraysum(ar):
    return sum(ar)

n = int(input())
ar = list(map(int, input().split()))

if n < 0 or n > 1000:
    print("Invalid array size.")
    exit()

for i in ar:
    if i < 0 or i > 1000:
        print("Elements should be between 0 and 1000.")
        exit()

result = simplearraysum(ar)
print(result)
