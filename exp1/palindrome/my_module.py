def Palindrome(string):
    if isinstance(string, (int,float))==True:
        raise TypeError("Enter a valid integer type string!") 
    s= "".join(char.lower() for char in string if char.isalnum())
    if s==s[::-1]:
        return s
  