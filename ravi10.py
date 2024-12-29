n=int(input())
i=0
j=0
lst=[]
while i<n:
    for j in range(n):
        e=int(input())
        print(e)
        j=j+1
        lst.append(str(e))
    print(list(lst))
    print(sep=' ')
    i=i+1
p1=lst[((n-1)*(n-1))]
p2=(int(lst[0]))*(int(p1))*(int(lst[p1+((n-1)*(n-1))]))
print(p2)
p1=int(lst[0])*int(lst[3])
print(p1)
