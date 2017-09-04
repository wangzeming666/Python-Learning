class Human:
  def __init__(self, n, a):
    self.name = n
    self.age = a
  def __repr__(self):
    return "Human('%s', %d)" %(self.name, self.age)
  
  def __str__(self):
    return "Human:name:"  + self.name+"..."
    
h1 = Human("abc", 18)
s1 = repr(h1)
h3 = eval(s1)
print("h3:", h3)
print(s1)
print(repr(h1))
print(str(h1))

