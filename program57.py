n,repeat=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
c=0
for i in range(n):
      if list[i]==repeat:
              c=c+1
print c
