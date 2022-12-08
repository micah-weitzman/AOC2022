import numpy as np

Matrix = np.ndarray

def make_int_matrix(str_data: list[str]) -> Matrix:
  int_matrix =  np.array(
    [
      np.array([int(i) for i in row])
      for row in str_data
    ]
  )
  return int_matrix


def viewable(val, data):
  arr = list(map(lambda y: y < val, data))
  if all(arr):
    return len(arr)
  else:
    return arr.index(False) + 1


def num_visible(data: np.ndarray) -> np.ndarray:
  is_visible = [0 for _ in data]
  
  for i, n in enumerate(data):
    if i == 0 or i == len(data) - 1:
      pass
    else:
      left = data[:i][::-1]
      right = data[i+1:]
      is_visible[i] = viewable(n, left) * viewable(n, right)

  return np.array(is_visible)



def total_visible(data: list[str]) -> int: 
  matrix = make_int_matrix(data)
  # print(matrix)

  vis_matrix: np.ndarray = np.zeros(matrix.shape)

  for i in range(len(matrix)):
    row = matrix[i]
    num_vis = num_visible(row)
    vis_matrix[i] = num_vis


  for i in range(1, len(matrix) - 1):
    col = matrix[:,i]
    num_vis = num_visible(col)
    vis_matrix[:,i] = vis_matrix[:,i] * num_vis


  return int(max([row.max() for row in vis_matrix]))


def run():

  data = []
  
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(l.strip())
      pass

  total = total_visible(data)
  
  print(total)


def test():
  test_data = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
  ]
  print(total_visible(test_data))

if __name__ == '__main__':
  run()
  # test()