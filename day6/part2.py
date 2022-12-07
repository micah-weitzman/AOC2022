

LEN = 14


def get_answer(s: str):
  for i in range(LEN-1,len(s)):
    if past_4 := set(s[i-LEN:i]):
      if len(past_4) == LEN:
        return i
  return 0


def run():
  
  with open('file.txt', 'r') as f:
    l = f.readline()
    # print(l)
    print(get_answer(l))  
  


def test():
  print(get_answer("bvwbjplbgvbhsrlpgdmjqwftvncz")) # 5
  print(get_answer("nppdvjthqldpwncqszvftbrmjlhg")) # 6
  print(get_answer("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")) # 10
  print(get_answer("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")) # 11
  
  
if __name__ == '__main__':
  run()