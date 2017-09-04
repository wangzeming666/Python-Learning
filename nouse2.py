class MyNumber:
  def __init__(self, value):
    self.data = value
    
  def __str__(self):
    return str(self.data)
    
  def __add__(self, rhs):
    return self.data + rhs.data
    
n1 = MyNumber(100)
n2 = MyNumber(200)
print(n1)
print(n2)
n3 = n1 + n2
print(n3)
