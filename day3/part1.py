

def run():
  total = 0

  alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

  with open('file.txt', 'r') as f:
    while line := f.readline().strip():
      first, second = line[:len(line)//2], line[len(line)//2:]
      x = list(set(first).intersection(set(second)))[0]
      
      total += alph.index(x) + 1
      
  print(total)

if __name__ == '__main__':
  run()