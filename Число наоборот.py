#import sys
#sys.stdin = open('input.txt','r')
#sys.stdout = open('output.txt','w')
a=int(input())
q=a%10
w=a//100%10
e=a//1000%100
r=a//10000%1000
t=a//100000%10000
y=a//1000000%100000
u=a//10000000%1000000
i=a//100000000%10000000
o=a//1000000000

p=q*1000000000+w*100000000+e*10000000+r*1000000+t*100000+y*10000+u*100+i*10+o

if a<0:
    print(-p)
else:
    print(p)