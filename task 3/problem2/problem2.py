n = int(input())
arr = list(map(int, input().split()))
sum = 0

if n>1000:
    print("error")

for i in arr:
    if 1 <= n <= 1000:
        sum +=i
        
print(sum)                
