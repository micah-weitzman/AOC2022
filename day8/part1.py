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


def row_visible(data: np.ndarray) -> np.ndarray:
  is_visible = [False for _ in data]
  
  for i, n in enumerate(data):
    # first and last always true 
    if i == 0 or i == len(data) - 1:
      is_visible[i] = True
    else:
      left = [x < n for x in data[:i]]
      right = [x < n for x in data[i+1:]]
      if all(left) or all(right):
        is_visible[i] = True
  
  return np.array(is_visible)



def total_visible(data: list[str]) -> int: 
  matrix = make_int_matrix(data)
  vis_matrix: np.ndarray = np.zeros(matrix.shape, dtype=bool)

  vis_matrix[0] = np.array([True for _ in matrix[0]])
  vis_matrix[-1] = np.array([True for _ in matrix[0]])

  for i in range(1, len(matrix) - 1):
    row = matrix[i]
    vis = row_visible(row)
    vis_matrix[i] = vis

  for i in range(1, len(matrix) - 1):
    col = matrix[:,i]
    is_vis = row_visible(col)
    vis_matrix[:,i] = vis_matrix[:,i] | is_vis


  return sum([row.sum() for row in vis_matrix])


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
    '25912',
    '65832',
    '33549',
    '35390',
  ]
  print(total_visible(test_data))

if __name__ == '__main__':
  run()
  # test()