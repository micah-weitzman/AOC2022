
score = 0

with open('file.txt', 'r') as f:
  while line := f.readline():
    opp, my = line.strip().split(' ')
    
    if my == 'X':
      if opp == 'A':
        score += 3
      if opp == 'B':
        score += 1
      if opp == 'C':
        score += 2
    if my == 'Y':
      score += 3
      if opp == 'A':
        score += 1
      if opp == 'B':
        score += 2
      if opp == 'C':
        score += 3
    if my == 'Z':
      score += 6
      if opp == 'A':
        score += 2
      if opp == 'B':
        score += 3
      if opp == 'C':
        score += 1
        
print(score)