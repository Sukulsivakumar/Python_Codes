def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
  
a = int(input())
b = int(input())
print(gcd(a,b))