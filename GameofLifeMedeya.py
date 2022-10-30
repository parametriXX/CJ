def randomizer():
    el = (__import__('random').random())
    return "М" if el < 0.25 else "Ф" if el >= 0.25 and el < 0.5 else "*" if el >= 0.5 and el < 0.75 else 0
class Field:
  def __init__(self, a1, a2, l, w): self.a1, self.a2, self.l, self.w = a1, a2, l, w
  def __str__(self):
    for i in range (1, self.w):
      for j in range(1, self.l):
        print("\033[31m{}\033[1m".format("М"), end = " ") if self.a1[i][j] == "М" else print("\033[33m{}\033[1m".format("Ф"), end = " ") if self.a1[i][j] == "Ф" else  print("\033[30m{}\033[1m".format("*"), end = " ") if self.a1[i][j] == "*" else print("\033[37m{}\033[1m".format(0), end = " ")
      print()
  def coordinates(self, x, y): 
    for x1, y1 in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)): yield x  + x1, y + y1
  def next(self):
    for i in range(self.w):
      for j in range(self.l):
          self.sq = Cell(self.a1, self.a2, self.l, self.w, *[k for k in self.coordinates(i, j)], (i, j), self.a1[i][j]); self.sq.redirect()
    self.a1 = self.a2; self.a2 = [[1]*(self.w + 2) for _ in range(self.l + 2)]
    for i in range(1, self.w + 1):
      for j in range(1, self.l + 1):
        self.a2[i][j] = 0
class Cell(Field):
  def __init__(self, a1, a2, l, w, n1, n2, n3, n4, n5, n6, n7, n8, n9, nCurrent):
    self.a1, self.a2, self.l, self.w,  self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.nCurrent = a1, a2, l, w, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8], n9, nCurrent
  def redirect(self):
    sq = Maniac(self.a1, self.a2, self.l, self.w, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8,self.n9 ,self.nCurrent) if self.nCurrent == "М" else Frank(self.a1, self.a2, self.l, self.w, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9 ,self.nCurrent) if self.nCurrent == "Ф" else Civilian(self.a1, self.a2, self.l, self.w, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9, self.nCurrent)
class Maniac(Cell):
  def __init__(self, a1, a2, l, w, n1, n2, n3, n4, n5, n6, n7, n8, n9, nCurrent):
      self.a1, self.a2, self.l, self.w, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.nCurrent = a1, a2, l, w, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8], n9, nCurrent
      if [self.a1[i[0]][i[1]] for i in self.array].count("М") ==  0 and [self.a1[i[0]][i[1]] for i in self.array].count("Ф") ==  0 and [self.a1[i[0]][i[1]] for i in self.array].count("*") == 0: i, j = self.n9; self.a2[i][j] = 0
      else:
        for k in self.array:
          i, j = k
          self.a2[i][j] = 0 if (__import__('random').random()) >= 0.25 else self.a1[i][j]
        x, y = self.n9; self.a2[x][y] = "М"
class Frank(Cell):
  def __init__(self, a1, a2, l, w, n1, n2, n3, n4, n5, n6, n7, n8, n9, nCurrent):
      self.a1, self.a2, self.l, self.w, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.nCurrent = a1, a2, l, w, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8], n9, nCurrent
      if [self.a1[i[0]][i[1]] for i in self.array].count(0) >= 1:
        for k in self.array:
          i, j = k
          if self.a1[i][j] == "М" and (__import__('random').random()) >= 0.25: x, y = self.n9; self.a2[x][y] = 0
          elif (__import__('random').random()) >= 0.1 and self.a1[i][j] == 0: self.a2[i][j] = randomizer()
          else: self.a2[i][j] = self.a1[i][j]
        x, y = self.n9; self.a2[x][y] = "Ф"
      else: x, y = self.n9; self.a2[x][y] = 0
class Civilian(Cell):
  def __init__(self, a1, a2, l, w ,n1, n2, n3, n4, n5, n6, n7, n8, n9, nCurrent):
      self.a1, self.a2, self.l, self.w, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.array, self.n9, self.nCurrent = a1, a2, l, w, n1, n2, n3, n4, n5, n6, n7, n8, [n1, n2, n3, n4, n5, n6, n7, n8], n9, nCurrent
      for k in self.array:
        i, j = k; x, y = n9
        self.a2[x][y] = 0 if self.a1[i][j] == "М" and (__import__('random').random()) >= 0.25 else "*"
N, M = map(int, input().split()); a1 = [[1]*(N + 2) for g in range(M + 2)]
for i in range(1, M + 1):
  for j in range(1, N + 1):
    a1[i][j] = randomizer()
a2 = [[0]*(N + 2) for g in range(M + 2)]; a = Field(a1, a2, N + 1, M + 1)
