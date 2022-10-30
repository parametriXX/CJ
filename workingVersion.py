def choose():
    x = (__import__('random').random())
    return "М" if x < 0.2 else return "Ф" if  if x >= 0.2 and x < 0.4 else return "*" if if x >= 0.4 and x < 0.7 else return 0
    if x >= 0.2 and x < 0.4: return "Ф"                       expr1 if condition1 else expr2 if condition2 else expr-n if condition-n else expr
    if x >= 0.4 and x < 0.7: return "*"
    else: return 0
class Field:
  def __init__(self, a1, a2, length, width): self.a1, self.a2, self.length, self.width = a1, a2, length, width
  def strop(self):
    for i in range (1, self.width):
      for j in range(1, self.length):
        if self.a1[i][j] == "М": print("\033[34m{}\033[1m".format("М"), end = " ")
        if self.a1[i][j] == "Ф": print("\033[35m{}\033[1m".format("Ф"), end = " ")
        if self.a1[i][j] == "*": print("\033[30m{}\033[1m".format("*"), end = " ")
        if self.a1[i][j] == 0: print("\033[37m{}\033[1m".format(0), end = " ")
      print()
  def neighbours(self, x, y): 
    for dx, dy in ((0, 1),(1, 1),(1, 0),(1, -1),(0, -1),(-1, -1),(-1, 0),(-1, 1)): yield x  + dx, y + dy
  def next(self):
    for i in range(self.width):
      for j in range(self.length):
          self.sq = Cell(self.a1, self.a2, self.length, self.width, *[k for k in self.neighbours(i, j)], (i, j), self.a1[i][j]); self.sq.distribute()
    self.a1 = self.a2; self.a2 = [[1]*(self.width+2) for g in range(self.length+2)]
    for i in range(1, self.width + 1):
      for j in range(1, self.length + 1):
        self.a2[i][j] = 0
class Cell(Field):
  def __init__(self, a1, a2, length, width, n1, n2, n3, n4, n5, n6, n7, n8, n9, n_main):
    self.a1, self.a2, self.length, self.width,  self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.n_main = a1, a2, length, width, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8], n9, n_main
  def distribute(self):
    if self.n_main == "М": sq = Maniac(self.a1, self.a2, self.length, self.width, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8,self.n9 ,self.n_main)
    if self.n_main == "Ф": sq = Frank(self.a1, self.a2, self.length, self.width, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9 ,self.n_main)
    if self.n_main == "*": sq = Civilian(self.a1, self.a2, self.length, self.width, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9, self.n_main)
class Maniac(Cell):
  def __init__(self, a1, a2, length, width, n1, n2, n3, n4, n5, n6, n7, n8, n9, n_main):
      self.a1, self.a2, self.length, self.width, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.n_main = a1, a2, length, width, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8],n9,n_main
      if [self.a1[i[0]][i[1]] for i in self.array].count("М") ==  0 and [self.a1[i[0]][i[1]] for i in self.array].count("Ф") ==  0 and [self.a1[i[0]][i[1]] for i in self.array].count("*") == 0: i, j = self.n9; self.a2[i][j] = 0
      else:
        for k in self.array:
          i, j = k
          if (__import__('random').random()) >= 0.25: self.a2[i][j] = 0
          else: self.a2[i][j] = self.a1[i][j]
        x, y = self.n9; self.a2[x][y] = "М"
class Frank(Cell):
  def __init__(self, a1, a2, length, width, n1, n2, n3, n4, n5, n6, n7, n8, n9, n_main):
      self.a1, self.a2, self.length, self.width, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.n_main = a1, a2, length, width, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8], n9, n_main
      if [self.a1[i[0]][i[1]] for i in self.array].count(0) >= 1:
        for k in self.array:
          i, j = k
          if self.a1[i][j] == "М" and (__import__('random').random()) >= 0.25: x, y = self.n9; self.a2[x][y] = 0
          elif (__import__('random').random()) >= 0.1 and self.a1[i][j] == 0: self.a2[i][j] = choose()
          else: self.a2[i][j] = self.a1[i][j]
        x, y = self.n9; self.a2[x][y] = "Ф"
      else: x, y = self.n9; self.a2[x][y] = 0
class Civilian(Cell):
  def __init__(self, a1, a2, length, width ,n1, n2, n3, n4, n5, n6, n7, n8, n9, n_main):
      self.a1, self.a2, self.length, self.width, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.n_main = a1, a2, length, width, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8], n9, n_main
      for k in self.array:
        i, j = k
        if self.a1[i][j] == "М" and (__import__('random').random()) >= 0.25: x, y = self.n9; self.a2[x][y] = 0;
        else: x, y = self.n9; self.a2[x][y] = "*"
n, m = map(int, input().split())
a1 = [[1]*(n+2) for g in range(m+2)]
for i in range(1, m+1):
  for j in range(1, n+1):
    a1[i][j] = choose()
a2 = [[0]*(n+2) for g in range(m+2)]
a = Field(a1, a2, n+1, m+1)
a.next()
a.strop()     
print()
a.next()
a.strop()
print()
a.next()
a.strop()     
print()
