import re

LINE = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')


def tuning_freq(x,y):
  return x * 4_000_000 + y

def manhat_dist(p1, p2):
  diff_x = abs(p1[0] - p2[0])
  diff_y = abs(p1[1] - p2[1])
  return diff_x + diff_y

def process_line(l, Y):
  m = LINE.search(l)  
  sensor_x = int(m.group(1))
  sensor_y = int(m.group(2))
  beacon_x = int(m.group(3))
  beacon_y = int(m.group(4))

  diff_x = abs(sensor_x - beacon_x)
  diff_y = abs(sensor_y - beacon_y)

  dist = diff_x + diff_y 

  pts = []
  for x in range(sensor_x - dist, sensor_x + dist + 1):
    for y in range(sensor_y - dist, sensor_y + dist + 1):
      if manhat_dist((x,y), (sensor_x, sensor_y)) <= dist:
        pts.append((x,y))

  return pts

def run():
  Y = 4_000_000 + 1
  data = [] 
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(l)

  S = set()
  for l in data:
    S.union(process_line(l, Y))

  U = []
  for x in range(Y):
    for y in range(Y):
      U.append((x,y))

  U = set(U)

  print(U.difference(S))


if __name__ == '__main__':
  run()