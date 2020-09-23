i = int(input())
j = list(map(int,input().split()))
k = set(j)
a=0

for x in k:
    if j.count(x)%2 == 0:
        a = a + int(j.count(x)/2)
    elif j.count(x)>2 :
        a = a + int(j.count(i)//2)

print(a)