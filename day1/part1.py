
def run():
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

  print(max(total))
  
if __name__ == '__main__':
  run()