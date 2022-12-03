
score = 0

with open('file.txt', 'r') as f:
  while line := f.readline():
    opp, my = line.strip().split(' ')
    
    if my == 'X':
      score += 1
      if opp == 'A':
        score += 3
      if opp == 'C':
        score += 6
    if my == 'Y':
      score += 2
      if opp == 'A':
        score += 6
      if opp == 'B':
        score += 3
    if my == 'Z':
      score +=3
      if opp == 'B':
        score += 6
      if opp == 'C':
        score += 3
        
print(score)