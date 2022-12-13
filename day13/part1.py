import itertools

GOOD = 0 
BAD = 1 
INCOMPLETE = 2 

def check_pair(l, r):
  if type(l) == int and type(r) == int:
    if l < r:
      return GOOD
    if l > r:
      return BAD
    return INCOMPLETE
  
  if type(l) == list and type(r) == list:
    for x,y in itertools.zip_longest(l, r):
      if x is None:
        return GOOD
      if y is None:
        return BAD
      foo = check_pair(x, y)
      if foo == INCOMPLETE:
        continue
      else:
        return foo
    return INCOMPLETE


  if type(l) == int and type(r) == list:
    return check_pair([l], r)

  if type(l) == list and type(r) == int:
    return check_pair(l, [r])
  
  raise ValueError("Something went wrong")



def run():
  total = 0
  with open('file.txt', 'r') as f:
    i = 0 
    while l := f.readline():
      i += 1
      l1 = eval(f.readline())
      l2 = eval(f.readline())

      if check_pair(l1,l2) == GOOD:
        print(i)
        total += i

  print(total)


if __name__ == '__main__':
  run()