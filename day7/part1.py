import re

CD = re.compile(r"\$ cd (.+)")
LS = re.compile(r"\$ ls")

DIR = re.compile(r"dir (.+)")
FILE = re.compile(r"(\d+) (.+)")


class Node: 
  def __init__(self, name):
    self.childDirs: 'dict[str, Node]' = {}
    self.size = 0
    self.name = name
    
  def add_dir(self, new_name, path):
    if len(path) == 0:
      new_node = Node(new_name)
      self.childDirs[new_name] = new_node
      return 
    self.childDirs[path[0]].add_dir(new_name, path[1:])

  def increase_size(self, size, path):
    if len(path) == 0:
      self.size += size
      return 
    
    dir_name = path[0]
    if len(path) == 1:
      self.childDirs[dir_name].size += size
    else:
      self.childDirs[dir_name].increase_size(size, path[1:])
      
  def total_size(self):
    total_size = 0 + self.size
    for _,v in self.childDirs.items():
      total_size += v.total_size()
    return total_size
  
  def size_less_than(self, targe_size):
    total = 0
    my_size = self.total_size()
    if my_size <= targe_size:
      total += my_size
      
    for k,v in self.childDirs.items():
      total += v.size_less_than(targe_size)
      
    return total
  
  def __repr__(self):
    start =  f"Node({self.name}, size={self.size}\n"
    for _,v in self.childDirs.items():
      start += str(v)
      
    start += ")"

def run():
  
  curr_dir: 'list[str]' = []
  root = Node('/')
  
  with open('file.txt', 'r') as f:
    while l := f.readline():
      
      if m := CD.search(l):
        new_dir = m.group(1)
        
        if new_dir == "..":
          curr_dir = curr_dir[:-1]
        else:
          curr_dir.append(new_dir)

      if m := LS.search(l):
        pass

      if m := DIR.search(l):
        dir_name = m.group(1)
        root.add_dir(dir_name, curr_dir)

      if m := FILE.search(l):
        size = int(m.group(1))
        filename = m.group(2)
        root.increase_size(size, curr_dir)
        
  print(root.size_less_than(100000))
  
if __name__ == '__main__':
  run()