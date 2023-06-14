#code
n=int(input()) 

while n>0:

    size=int(input())

    a = list(map(int,input().strip().split(' ')))

    d={}

    for i in a:

        if i not in d:

            d[i]=1

        else:

            d[i]+=1

    sorted_A = sorted(a, key=lambda x: (-d[x], x))

    for i in sorted_A:

        print(i,end=" ")

    print()

    n-=1