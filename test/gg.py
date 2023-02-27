class Shape:
  def __init__(self, base, hight):
    self.base = base
    self.hight = hight
  def area(self):
    return self.base * self.hight
  def mohit(self):
    return self.base * 2 + self.hight * 2
class square(Shape):
  def __init__(self,base,hight):
    super().__init__(base,hight)
class mostatil(Shape):
  def __init__(self, base, hight):
    super(). __init__(base, hight)
class triangle(Shape):
  def __init__(self, base, hight, a, b, c):
    super(). __init__(base, hight)
    self.a = a
    self.b = b
    self.c = c
  def area(self):
    return (self.hight * self.base)/2
  def mohit(self):
    return self.a+self.b+self.c

    
Shapes = (square(5), mostatil(3,4), triangle(4,3,3,5,4))
for shape in shapes:
  print(shape.area(),shape.mohit())