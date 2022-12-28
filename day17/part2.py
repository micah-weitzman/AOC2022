import itertools
import copy
import re
from collections import defaultdict

test_data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

class Shape:
  def __init__(self, shape):
    pattern, symbol = shape
    self.pattern = pattern
    self.height = len(pattern)
    self.width = len(pattern[0])
    self.x = 0
    self.y = 0
    self.symbol = symbol


bar = ([['-','-','-','-']], '-')
plus =  ([
    ['.', '+', '.'],
    ['+', '+', '+'],
    ['.', '+', '.'],
  ], '+')
ell = ([
  ['.','.','⅃'],
  ['.','.','⅃'],
  ['⅃','⅃','⅃'],
], '⅃')
line = ([['l'],['l'],['l'],['l']], 'l')
square = ([['□', '□'],['□', '□']], '□')

SYMBOLS = '-l□⅃+'
SYMBOLS_RE = re.compile(r'-|l|□|⅃|\+')

def default_():
  return ['.','.','.','.','.','.','.']

class State:
  def __init__(self):
    self.curr_block = None
    self.state = defaultdict(default_)
    self.top = 0

  def add_shape(self, shape: Shape):
    self.curr_block = shape
    shape.x = 2
    shape.y = self.top+3
    self.top = shape.y + shape.height

  def move_down(self):
    # test to see if can move down 1
    try:
      self.curr_block.y -= 1
      for y, row in enumerate(self.curr_block.pattern[::-1]):
        for x, val in enumerate(row):
          if self.state[self.curr_block.y + y][self.curr_block.x + x] in SYMBOLS and val in SYMBOLS or self.curr_block.y + y < 0:
            raise LookupError
    except:
      self.curr_block.y += 1
      for y, row in enumerate(self.curr_block.pattern[::-1]):
        for x, val in enumerate(row):
          if val in SYMBOLS:
            self.state [self.curr_block.y + y][self.curr_block.x + x] = val
      self.curr_block = None

      for k in sorted(i for i in range(max(1,self.top-50), self.top + 50)):
        if '.' not in self.state[k] and self.state[k+1] == ['.','.','.','.','.','.','.']:
          print('HERE')
        r = ''.join(self.state[k])
        if not SYMBOLS_RE.search(r):
          self.top = k
          break
      raise LookupError


  def move_shape(self, direction):
    self.top = self.curr_block.y + self.curr_block.height
    if self.curr_block is None:
      return
    # LEFT 
    if direction == '<':
      if self.curr_block.x == 0:
        return
      else:
        try:
          self.curr_block.x -= 1
          for y, row in enumerate(self.curr_block.pattern[::-1]):
            for x, val in enumerate(row):
              if self.state[self.curr_block.y + y][self.curr_block.x + x] in SYMBOLS and val in SYMBOLS:
                raise LookupError
        except:
          self.curr_block.x += 1
          return
    # RIGHT
    if direction == '>':
      if self.curr_block.x + self.curr_block.width > 6:
        return
      else:
        try:
          self.curr_block.x += 1
          for y, row in enumerate(self.curr_block.pattern[::-1]):
            for x, val in enumerate(row):
              if self.state[self.curr_block.y + y][self.curr_block.x + x] in SYMBOLS and val in SYMBOLS:
                raise LookupError
        except:
          self.curr_block.x -= 1
          return
  
  def print(self, length=30, start=0):
    pass
    new_state = copy.deepcopy([self.state[i] for i in range(start,start+length)])
    if self.curr_block is not None:
      for y, row in enumerate(self.curr_block.pattern[::-1]):
        for x, val in enumerate(row):
          new_state[self.curr_block.y + y][self.curr_block.x + x] = '@' if val in SYMBOLS else '.'

    for i,v in enumerate(new_state[::-1]):
      print('|' + ''.join(v) + '|' + f' {len(new_state) - i+start}')
    print('+-------+')
    print("\n")

def run():
  data = []
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(l)
  data = data[0]
  direction = itertools.cycle(data)

  shapes = itertools.cycle([bar, plus, ell, line, square])

  s = State()

  for r in range(2022):
    if r % 10000 == 0:
      print(f"{r:,}")
    new_shape = Shape(next(shapes))
    s.add_shape(new_shape)
    while True:
      try:
        s.move_shape(next(direction))
        s.move_down()
      except Exception as e:
        break

  s.print(200, 2900)

  print(s.top)


if __name__ == '__main__':
  run()