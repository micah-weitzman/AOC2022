import re

MATCH = re.compile(r"(\d+),(\d+)")


def make_maze(data):
  all_coords = []
  for l in data:
    coords = [(int(x),int(y)) for x,y in MATCH.findall(l)]

    for i in range(len(coords) - 1):
      start = coords[i]
      end = coords[i+1]
      if start[0] - end[0] == 0:
        # diff y
        iter_start = min(start[1], end[1])
        iter_end = max(start[1], end[1]) + 1
        for v in range(iter_start, iter_end):
          all_coords.append((start[0], v))
      elif start[1] - end[1] == 0:
        iter_start = min(start[0], end[0])
        iter_end = max(start[0], end[0]) + 1
        for v in range(iter_start, iter_end):
          all_coords.append((v, start[1]))
  
  all_coords = list(set(all_coords))

  all_coords.append((500, 0))
  # min_x = min([x[0] for x in coords])
  min_x = 200
  max_y = max([z[1] for z in all_coords])

  max_x = max([x[0] for x in all_coords]) + 3 * max_y 
  
  coords = [(x-min_x, y) for x,y in all_coords]
  

  

  to_print = [["." for _ in range(max_x+1)] for _ in range(max_y+3)]

  for foo,bar in coords:
    to_print[bar][foo] = '#'

  to_print[-1] = ['#' for _ in range(len(to_print[0]))]

  start_coord_x = to_print[0].index('#')
  to_print[0][start_coord_x] = '.'
  return start_coord_x, to_print


def drop_sand(x_coord, y_coord, maze):
  if x_coord < 0 or x_coord >= len(maze[0]) or y_coord < 0 or y_coord >= len(maze):
    raise IndexError
  if maze[y_coord][x_coord] == '.':
    down = maze[y_coord + 1][x_coord]
    left = maze[y_coord + 1][x_coord - 1]
    right = maze[y_coord + 1][x_coord + 1]
    if down == '.':
      drop_sand(x_coord, y_coord+1, maze)
    elif left == '.':
      drop_sand(x_coord-1, y_coord+1, maze)
    elif right == '.':
      drop_sand(x_coord+1, y_coord+1, maze)
    else:
      maze[y_coord][x_coord] = 'o'
    return 
  
  # for row in maze:
  #   print(''.join(row))
  # print(x_coord, y_coord)
  raise LookupError("Something bad happened")

def run():
  data = []
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(l)

  start_x, maze = make_maze(data)
  maze[0][start_x] = '.'

  i = 0 
  while True:
    try:
      if maze[0][start_x] == 'o':
        raise ValueError
      drop_sand(start_x, 0, maze)
      i += 1
    except:
      break
  
  for row in maze:
    print(''.join(row))
  print(i)

if __name__ == '__main__':
  run()