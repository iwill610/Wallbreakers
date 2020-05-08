 if n<0:
            x=(1/x)
            n=abs(n)
        def factor(x,n):
            if n==1:
                return x
            if n==0:
                return 1
            factorevens=factor(x,n//2)
            if n%2==1:
                return factorevens*factorevens*x
            else:
                return factorevens*factorevens
        return factor(x,n)