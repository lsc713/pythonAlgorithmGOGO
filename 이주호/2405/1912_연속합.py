n=int(input())
arr=list(map(int,input().split()))
prefix = [-1000 for _ in range(n+1)]
for i in range(n):
    prefix[i+1] = max(prefix[i] + arr[i],arr[i])


print(max(prefix))