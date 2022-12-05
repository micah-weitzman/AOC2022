from collections import deque
import re
"""
                  [B]     [L]     [S]
          [Q] [J] [C]     [W]     [F]
      [F] [T] [B] [D]     [P]     [P]
      [S] [J] [Z] [T]     [B] [C] [H]
      [L] [H] [H] [Z] [G] [Z] [G] [R]
  [R] [H] [D] [R] [F] [C] [V] [Q] [T]
  [C] [J] [M] [G] [P] [H] [N] [J] [D]
  [H] [B] [R] [S] [R] [T] [S] [R] [L]
   1   2   3   4   5   6   7   8   9
"""

# b1 = deque(["R", "C", "H"][::-1])
# b2 = deque(["F","S","L","H","J","B"][::-1])
# b3 = deque(["Q","T","J","H","D","M","R"][::-1])
# b4 = deque(["J","B","Z","H","R","G","S"][::-1])
# b5 = deque(["B","C","D","T","Z","F","P","R"][::-1])
# b6 = deque(["G","C","H","T"][::-1])
# b7 = deque(["L","W","P","B","Z","V","N","S"][::-1])
# b8 = deque(["C","G","Q","J","R"][::-1])
# b9 = deque(["S","F","P","H","R","T","D","L"][::-1])

# boxes = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

def run():
  boxes = [deque() for _ in range(9)]

  def process_chart(line: str):
    m = re.split(r"\[(\w)\]|\s{4}", line)[1:-1]
    letters = [i for i in m if i != None and i != ' ']
    
    for i, letter in enumerate(letters):
      if letter.isalpha():
        boxes[i].appendleft(letter)
    

  def process_input(line: str):
    m = re.search(r"move (\d+) from (\d) to (\d)", line)
    num_move = int(m.group(1))
    src = int(m.group(2))
    dst = int(m.group(3))
    
    src_deq = boxes[src - 1]
    dst_deq = boxes[dst - 1]
    
    to_move = []
    
    for i in range(num_move):
      to_move.append(src_deq.pop())

    dst_deq.extend(to_move)
    
    
  with open('file.txt', 'r') as f:
    while l := f.readline():
      if re.search(r"move", l):
        process_input(l)

      elif re.search(r"\[\w\]", l):
        process_chart(l)


  for b in boxes:
    print(b.pop(), end='')
    
if __name__ == '__main__':
  run()