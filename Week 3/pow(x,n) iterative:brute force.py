if n<0:
            x=(1/x)
            n=abs(n)
        num = 1
        
        while n:
            if n%2==1:
                num*=x
                n-=1
            else:
                x=x*x
                n=n//2
      
        return num