
def get_neighbors(point):
  x,y,z = point
  return [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]

class Edge:
  def __init__(self, left, right):
    self._left = left
    self._right = right
    self.left = hash(left)
    self.right = hash(right)
  
  def __eq__(self, ob) -> bool:
    return (ob.left == self.left and ob.right == self.right) or \
      (ob.left == self.right and ob.right == self.left)

class Graph:
  def __init__(self, coords):
    self.coords = coords
    self.edges = []
    
    for block in coords:
      neighbors = get_neighbors(block)
      for n in neighbors:
        if n in coords:
          e = Edge(block, n)
          self.edges.append(e)

  
  def get_surface_area(self):
    all_edges = []
    for e in self.edges:
      if e not in all_edges:
        all_edges.append(e)

    return 6 * len(self.coords) - 2 * len(all_edges) 


def run():
  data = []
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(eval(f'({l.strip()})'))


  g = Graph(data)
  ans = g.get_surface_area()
  print(ans)


if __name__ == '__main__':
  run()