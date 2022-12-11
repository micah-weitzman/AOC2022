import re

MATCH = re.compile(r"(L|R|U|D) (\d+)")


def get_answer(instrs):
  head = [(0,0)]
  tail = [(0,0)]

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
       (h_x == t_x + 2  and h_y == t_y + 1):
      tail.append((t_x + 1, t_y + 1))

    elif (h_x == t_x - 1  and h_y == t_y + 2) or \
       (h_x == t_x - 2  and h_y == t_y + 1):
      tail.append((t_x - 1, t_y + 1))
      
    elif (h_x == t_x + 1  and h_y == t_y - 2) or \
       (h_x == t_x + 2  and h_y == t_y - 1):
      tail.append((t_x + 1, t_y - 1))
    
    elif (h_x == t_x - 1  and h_y == t_y - 2) or \
       (h_x == t_x - 2  and h_y == t_y - 1):
      tail.append((t_x - 1, t_y - 1))


  total_tail = len(set(tail))
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

if __name__ == '__main__':
  run()