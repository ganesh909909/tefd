f=open('C:\\Users\GOWRI\Desktop\python.txt','r')
p=open('java.txt')
g=str(f.read())
h=g.split()
o=str(p.read())
a=o.split()
n=set(h)&set(a)
m=set(h)^set(a)
print(m)
print(n)
