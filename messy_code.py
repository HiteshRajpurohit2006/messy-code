# BEFORE: the messy script
def f(l):
    t=0
    for i in range(0,len(l)):
        t=t+l[i]
    a=t/len(l)
    m=l[0]
    for x in l:
        if x>m:m=x
    n=l[0]
    for x in l:
        if x<n:n=x
    print("total",t,"avg",a,"max",m,"min",n)
f([300,500,1500,3000])
