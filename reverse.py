def interverse(n):
    ans=0
    while n>0:
        r=n%10
        ans=(ans*10)+r
        n=n/10
    return(ans)

n=input("enter a value:")
print interverse(n)
    
    

    
