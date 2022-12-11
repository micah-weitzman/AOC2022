import re

MATCH = re.compile(r"(L|R|U|D) (\d+)")


def get_follow(head):
  tail = [(0,0)]
  for h_x, h_y in head[1:]:
    t_x, t_y = tail[-1]
    if (h_x == t_x + 1 and h_y == t_y) or \
       (h_x == t_x + 1 and h_y == t_y + 1) or \
       (h_x == t_x + 1 and h_y == t_y - 1) or \
       (h_x == t_x - 1 and h_y == t_y) or \
       (h_x == t_x - 1 and h_y == t_y + 1) or \
       (h_x == t_x - 1 and h_y == t_y - 1) or \
       (h_x == t_x and h_y == t_y + 1) or \
       (h_x == t_x and h_y == t_y - 1) or \
       (h_x == t_x and h_y == t_y):
      tail.append((t_x, t_y))
      
    elif (h_x == t_x + 2 and h_y == t_y):
      tail.append((t_x + 1, t_y))
    elif (h_x == t_x - 2 and h_y == t_y):
      tail.append((t_x - 1, t_y))
    elif (h_x == t_x  and h_y == t_y + 2):
      tail.append((t_x, t_y + 1))
    elif (h_x == t_x  and h_y == t_y - 2):
      tail.append((t_x, t_y - 1))
      
    elif (h_x == t_x + 1  and h_y == t_y + 2) or \
       (h_x == t_x + 2  and h_y == t_y + 2) or \
       (h_x == t_x + 2  and h_y == t_y + 1):
      tail.append((t_x + 1, t_y + 1))

    elif (h_x == t_x - 1  and h_y == t_y + 2) or \
       (h_x == t_x - 2  and h_y == t_y + 2) or \
       (h_x == t_x - 2  and h_y == t_y + 1):
      tail.append((t_x - 1, t_y + 1))
      
    elif (h_x == t_x + 1  and h_y == t_y - 2) or \
       (h_x == t_x + 2  and h_y == t_y - 2) or \
       (h_x == t_x + 2  and h_y == t_y - 1):
      tail.append((t_x + 1, t_y - 1))
    
    elif (h_x == t_x - 1  and h_y == t_y - 2) or \
        (h_x == t_x - 2  and h_y == t_y - 2) or \
       (h_x == t_x - 2  and h_y == t_y - 1):
      tail.append((t_x - 1, t_y - 1))
  return tail 

def get_answer(instrs):
  head = [(0,0)]

  for dir, l in instrs:
    head_x, head_y = head[-1]
    for i in range(1, l+1):
      if dir == 'U':
        head.append((head_x, head_y + i))
      if dir == 'D':
        head.append((head_x, head_y - i))
      if dir == 'R':
        head.append((head_x + i, head_y))
      if dir == 'L':
        head.append((head_x - i, head_y))

  one = get_follow(head)
  two = get_follow(one)
  three = get_follow(two)
  four = get_follow(three)
  five = get_follow(four)
  six = get_follow(five)
  seven = get_follow(six)
  eight = get_follow(seven)
  nine = get_follow(eight) 

  # print(six)
  total_tail = len(set(nine))
  return total_tail

def run():
  instructions = []
  
  with open('file.txt', 'r') as f:
    while l := f.readline():
      m = MATCH.search(l)
      direction = m.group(1)
      length = int(m.group(2))
      instructions.append((direction, length))
  
  
  ans = get_answer(instructions)
  print(ans)
  
def test():
  instructions = [
    ('R', 5),
    ('U', 8),
    ('L', 8),
    ('D', 3),
    ('R', 17),
    ('D', 10),
    ('L', 25),
    ('U', 20),
  ]
  
  ans = get_answer(instructions)
  print(ans)

if __name__ == '__main__':
  # test()
  run()