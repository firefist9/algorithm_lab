def activity_selector(st,fi):
    A=[0]
    n=len(st)
    k=0

    for i in range(1,n):
       if st[i]>=fi[k]:
           A.append(i)
           k=i
    return A



#s=[1,3,0,5,3,5,6,8,8,2,12]
#f=[4,5,6,7,8,9,10,11,12,13,14]

#print(activity_selector(s,f))

