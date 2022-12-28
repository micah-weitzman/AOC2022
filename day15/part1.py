import re

LINE = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

Y = 2_000_000


def process_line(l):
  m = LINE.search(l)  
  sensor_x = int(m.group(1))
  sensor_y = int(m.group(2))
  beacon_x = int(m.group(3))
  beacon_y = int(m.group(4))

  diff_x = abs(sensor_x - beacon_x)
  diff_y = abs(sensor_y - beacon_y)

  dist = diff_x + diff_y 

  if sensor_y + dist >= Y or  sensor_y - dist <= Y:
    diff_to_y = abs(Y - sensor_y)
    diff_left = dist - diff_to_y
    pts = [x + sensor_x for x in range(-diff_left, diff_left + 1)]
    return pts

  return []


def run():
  data = [] 
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(l)

  
  S = set()
  for l in data:
    S = S.union(process_line(l))

  print(len(S) - 1) 

if __name__ == '__main__':
  run()