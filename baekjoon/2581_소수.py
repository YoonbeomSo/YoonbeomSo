M = int(input())
N = int(input())
sosu=[]
for i in range(M,N+1):
    check=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                check=1
                break
        if check==0:
            sosu.append(i)
if len(sosu)>0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)