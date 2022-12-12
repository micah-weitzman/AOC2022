import math

class Monkey:
  def __init__(self, items, op, test):
    self.items: list[int] = items
    self.op = op
    self.test = test
    self.num_checked = 0 
    
  def sim_round(self):
    if len(self.items) == 0:
      return None
    to_out = self.items.pop(0)
    new_val = self.op(to_out)
    new_val = math.floor(new_val / 3)
    monkey_num = self.test(new_val)
    
    self.num_checked += 1
    
    return (monkey_num, new_val)


def run():

  i0 = [56, 56, 92, 65, 71, 61, 79]
  op0 = lambda x : x * 7
  t0 = lambda x : 3 if (x % 3 == 0) else 7
  m0 = Monkey(i0, op0, t0)
  
  i1 = [61, 85]
  op1 = lambda x : x + 5
  t1 = lambda x : 6 if (x % 11 == 0) else 4
  m1 = Monkey(i1, op1, t1)
  
  i2 = [54, 96, 82, 78, 69]
  op2 = lambda x : x * x
  t2 = lambda x : 0 if (x % 7 == 0) else 7
  m2 = Monkey(i2, op2, t2)
  
  i3 = [57, 59, 65, 95] 
  op3 = lambda x : x + 4
  t3 = lambda x : 5 if (x%2==0) else 1 
  m3 = Monkey(i3, op3, t3)
  
  i4 = [62, 67, 80]
  op4 = lambda x : x * 17
  t4 = lambda x : 2 if (x % 19 == 0) else 6
  m4 = Monkey(i4, op4, t4)

  i5 = [91]
  op5 = lambda x : x + 7
  t5 = lambda x : 1 if (x % 5 == 0) else 4
  m5 = Monkey(i5, op5, t5)
  
  i6 = [79, 83, 64, 52, 77, 56, 63, 92]
  op6 = lambda x : x + 6
  t6 = lambda x : 2 if (x % 17 == 0) else 0
  m6 = Monkey(i6, op6, t6)
  
  i7 = [50, 97, 76, 96, 80, 56]
  op7 = lambda x : x + 3
  t7 = lambda x : 3 if (x % 13 == 0) else 5 
  m7 = Monkey(i7, op7, t7)
  
  all_monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]
  
  
  # i0 = [79, 98]
  # op0 = lambda x : x * 19
  # t0 = lambda x : 2 if (x % 23 == 0) else 3
  # m0 = Monkey(i0, op0, t0)
  
  # i1 = [54, 65, 75, 74]
  # op1 = lambda x : x + 6
  # t1 = lambda x : 2 if (x % 19 == 0) else 0
  # m1 = Monkey(i1, op1, t1)
  # i2 = [79, 60, 97]
  # op2 = lambda x : x * x
  # t2 = lambda x : 1 if (x % 13 == 0) else 3
  # m2 = Monkey(i2, op2, t2)
  # i3 = [74]
  # op3 = lambda x : x + 3 
  # t3 = lambda x : 0 if (x % 17 == 0) else 1
  # m3 = Monkey(i3, op3, t3)
  # all_monkeys = [m0, m1, m2, m3]
  
  for _ in range(20):
    for m in all_monkeys:
      while ans := m.sim_round():
        monkey_num, new_val = ans
        all_monkeys[monkey_num].items.append(new_val)
  
  
  all_checked = [m.num_checked for m in all_monkeys]
  
  all_checked = sorted(all_checked, reverse=True)

  print(all_checked[0] * all_checked[1])
  
  # for i,m in enumerate(all_monkeys):
  #   print(f'Monkey{i}: {m.items}')
  
  
if __name__ == '__main__':
  run()