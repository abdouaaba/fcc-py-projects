class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2*self.width + 2*self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    pic = ''
    for i in range(self.height):
      for j in range(self.width):
        pic += "*"
      pic += "\n"
    return pic

  def get_amount_inside(self, shape):
    times = 0
    if self.width > shape.width:
      if self.height > shape.height:
        n = int(self.height/shape.height) * int(self.width/shape.width)
        times += n
    return times

  def __str__(self):
    res = "Rectangle(width={}, height={})".format(self.width,self.height)
    return res
    
    

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length
  
  def set_side(self, length):
    self.set_width(length)
    self.set_height(length)

  def set_width(self, length):
    self.width = length
    self.height = length

  def set_height(self, length):
     self.width = length
     self.height = length
  
  def __str__(self):
    res = "Square(side={})".format(self.width)
    return res

