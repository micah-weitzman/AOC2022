import itertools
import functools

GOOD = -1
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
  TWO = [[2]]
  SIX = [[6]]
  data = [TWO, SIX]
  with open('file.txt', 'r') as f:
    while l := f.readline():
      l1 = eval(f.readline())
      l2 = eval(f.readline())
      data.append(l1)
      data.append(l2)

  sorted_data = sorted(data, key=functools.cmp_to_key(check_pair))
  ans = (sorted_data.index(TWO)+1) * (sorted_data.index(SIX)+1)
  print(ans)

if __name__ == '__main__':
  run()