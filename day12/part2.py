import queue

alph = 'abcdefghijklmnopqrstuvwxyz'
def a_to_i(letter):
  if letter == 'S':
    return 1
  if letter == 'E':
    return 26
  return alph.index(letter) + 1


def get_start_end(data):
  start = []
  end = None 

  for i, row in enumerate(data):
    for j, v in enumerate(row):
      if v == 'S' or v == 'a':
        start.append((j, i))
      elif v == 'E':
        end = (j, i)
  
  return start, end


class Graph:
  def __init__(self, data):
    self.vert = {}
    self.dist = {}

    for j, row in enumerate(data):
      for i, v in enumerate(row):
        loc = (i,j)
        self.dist[loc] = 0
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
          if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data):
            neighbor_val = data[y][x]
            if neighbor_val <= v + 1:
              if loc in self.vert.keys():
                self.vert[loc].append((x,y))
              else:
                self.vert[loc] = [(x,y)]
          if loc not in self.vert.keys():
            self.vert[loc] = []
    
  def get_dist(self, src, dst):

    visited = { k: False for k in self.vert.keys() }
    Q = queue.Queue()
    Q.put(src)
    visited[src] = True
    self.dist[src] = 0

    while not Q.empty():
      u = Q.get()
      for n in self.vert[u]:
          if visited[n]:
            continue
          self.dist[n] = self.dist[u] + 1
          Q.put(n)
          visited[n] = True

    return self.dist[dst]


def run():
  data = []
  
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append([x for x in l.strip()])

  start, end = get_start_end(data)
  m = [[a_to_i(v) for v in row] for row in data]
  G = Graph(m)
  
  d = min([G.get_dist(s, end) for s in start])
  
  print(d)

if __name__ == '__main__':
  run()