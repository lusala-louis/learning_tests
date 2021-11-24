class Rectangle:
    def __init__(self,c,l,w):
        self.color=c
        self.length=l
        self.width=w
    def area(self):
        self.area=self.length*self.width
        return self.area
    def perimeter(self):
        self.per=(2*self.length)+(2*self.width)
        return self.per
    def diagonal(self):
        self.diag=(self.length**2+self.width**2)**(1/2)
        return self.diag
myRect1=Rectangle('blue',5,7)
myRect2=Rectangle('black',8,4)
print('The Color of myRect1=',myRect1.color)
print('The Area of myRect1=',myRect1.area())
print('The Perimeter of myRect1=',myRect1.perimeter())
print('The Diagonal of myRect1 is=',myRect1.diagonal())