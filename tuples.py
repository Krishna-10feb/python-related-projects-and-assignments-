#tuple 
a=(1,2,3,4,5)
print(a)
a=10,20,30
print(a)
a[2]
a[-1]
b=(1,2,3,4,5,6,7,8,9)
print(b)
b[0:]
b[0:8]
b[-8:]
print(b)
a=(10,20,30,[40,50,60,])
a[3][1]=55
print(a)
#concatenating a tuple 
c=a+b
print(c)
#deleting a tuple
del(c)
print(c)
a=(1,1,1,1,2,3,4,5)
a.count(1)
print(a.count(1))
a.index(5)
print(a.index(5))
a.index(1)
print(a.indes(1))
#to change list to tuple 
a=[1,2,3]
print(a)
b=tuple(a)
print(b)
    
