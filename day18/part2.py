def get_neighbors(point):
  x,y,z = point
  return [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]


def get_outside(data):
  min_space = [min(c[i]-1 for c in data) for i in range(3)]
  max_space = [max(c[i]+1 for c in data) for i in range(3)]

  def is_in(point):
    return all(min_space[i] <= point[i] <= max_space[i] for i in range(3))

  outside = 0
  seen = set()
  queue = [tuple(max_space)]
  while queue:
    curr = queue.pop(0)
    if curr in data:
      outside += 1
      continue
    if curr not in seen:
      seen.add(curr)
      for n in get_neighbors(curr):
        if is_in(n):
          queue.append(n)
  return outside


def run():
  data = []
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(eval(f'({l.strip()})'))

  ans = get_outside(data)
  print(ans)


if __name__ == '__main__':
  run()