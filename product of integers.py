n=int(input('enter the number:'))
rev=1
while n>0:
    dig=n%10
    rev=rev*dig
    n=n//10
print(rev)