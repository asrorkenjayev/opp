class Shape:
    def __init__(self, n:int):
        self.n=n
    def linya(self):
        for i in range(self.n):
            print('*', end="")
    def tort_burchak(self):
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                if i==1 or j==1 or i==self.n or j==self.n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")    
            print()
    def uchburchak(self):
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                if (j==1) or (i==self.n) or (i == j):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")    
            print()
    
    
    
class Chiziq(Shape):
    def __init__(self, n):
        super().__init__(n)
    def chiqar(self):
        super().linya()    

class Tort_burchak(Shape):
    def __init__(self, n):
        super().__init__(n)
    def yoz(self):
        super().tort_burchak()

class Uchburchak(Shape):
    def __init__(self, n):
        super().__init__(n)
    def uch(self):
        super().uchburchak()

a=Chiziq(10)
a.chiqar()
print()
b=Tort_burchak(15)
b.yoz()
print()
c=Uchburchak(10)
c.uch()

