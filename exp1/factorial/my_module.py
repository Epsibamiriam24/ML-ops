def fact(n):
    if (n==0 or n==1):
        return 1
    if n<0:
        raise ValueError("Enter a valid positive number!")
    #for non-numeric type
    if isinstance(n, (int))!=True:
        raise TypeError("Enter a valid integer type number!")
    #for float numbers
    if isinstance(n, (int))!=True:
        raise TypeError("Enter a valid integer type number!")
    else:
        return n*fact(n-1)  


    
    





    