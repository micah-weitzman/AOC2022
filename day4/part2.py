
from dataclasses import dataclass
from typing import Tuple

def run():
  @dataclass
  class Range:
    start: int
    end: int


  def get_range(line: str): # -> Range
    left, right = line.split("-")
    return Range(start=int(left), end=int(right))

  def process_line(line: str): #  -> Tuple[Range, Range]
    fst, snd = line.strip().split(',')
    return (get_range(fst), get_range(snd))


  def check_overlap(left: Range, right: Range): # -> Bool
    cond1 = left.start >= right.start and left.start <= right.end
    cond2 = right.start >= left.start and right.start <= left.end
    
    return cond1 or cond2

  num_overlap = 0


  with open('file.txt', 'r') as f:
    while l := f.readline():
      ranges = process_line(l)
      if check_overlap(*ranges):
        num_overlap += 1
      
  print(num_overlap)


if __name__ == '__main__':
  run()