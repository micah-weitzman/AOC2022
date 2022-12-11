import re

ADDX = re.compile(r"addx (-?\d+)")
NOOP = re.compile(r"noop")

def run():
  addx = [1]
  stage = addx[-1]
  
  with open('file.txt', 'r') as f:
    while l := f.readline():
      if m := ADDX.search(l):
        addx.append(stage)
        addx.append(addx[-1])
        stage = addx[-1] + int(m.group(1))
        
      elif NOOP.search(l):
        addx.append(stage)
        stage = addx[-1]
        
  lst = [20, 60, 100, 140, 180, 220]
  
  total = [addx[x] * x for x in lst]
  # print(addx)
  print(sum(total))
  
  
  
if __name__ == '__main__':
  run()