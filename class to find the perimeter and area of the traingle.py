class Triangle:

    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def area(self):
        s=(self.a + self.b + self.c)/2
        return((s*(s-self.a)*(s-self.b)*(s-self.c))**0.5)
    def perimeter(self):
       return (self.a+self.b+self.c)

a=input("Enter the value of a = ")
b=input("Enter the value of b = ")
c=input("Enter the value of c = ")
t = Triangle(a, b, c)
print("area : {}".format(t.area()))
print("perimeter: {}".format(t.perimeter()))
