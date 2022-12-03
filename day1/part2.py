
data = {}

with open('day1\\file.txt', 'r') as f:
  count = 0 
  while l := f.readline():
    if l == '\n':
      count += 1
    else:
      if count in data.keys():
        data[count].append(int(l))
      else:
        data[count] = [int(l)]
        
total = [sum(lst) for lst in data.values()]
top_three = sorted(total, reverse=True)[0:3]

print(sum(top_three))