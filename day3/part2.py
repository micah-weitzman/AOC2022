total = 0

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('file.txt', 'r') as f:
  while fst := f.readline().strip():
    snd = f.readline().strip()
    thrd = f.readline().strip()
    x = list(set(fst).intersection(set(snd)).intersection(set(thrd)))[0]
    
    total += alph.index(x) + 1
    
print(total)