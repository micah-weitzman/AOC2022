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
          
  
  addx = addx[1:]
  out = []
  L = 40

  for i,v in enumerate(addx):
    if (i % L) == v or (i % L) == v+1 or (i % L) == v-1:
      out.append('#')
    else:
      out.append('.')

  for i in range(int((len(addx) - 1)/40) + 1):
    print(''.join(out[i*40:(i+1)*40]))
  
  
if __name__ == '__main__':
  run()