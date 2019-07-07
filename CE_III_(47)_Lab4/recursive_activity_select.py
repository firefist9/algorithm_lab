def activity_selector(st,fi,k,n):
    m=k+1
    
    while m<n and st[m]<fi[k] and k>=0:
        m=m+1
        
    if m<n:
        A.append(m)
        activity_selector(st,fi,m,n)
    else:
        return None

    return A    


#s=[1,3,0,5,3,5,6,8,8,2,12]
#f=[4,5,6,7,8,9,10,11,12,13,14]
A=[]                          

#print(activity_selector(s,f,-1,len(f)))
