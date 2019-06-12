def maxCoinSum(a, n):
  max_sum = 0

  matrix = [[[0, 0] for i in range(n)] for i in range(n)]

  for i in range(n):
    matrix[i][i][0] = a[i]

  for i in range(1, n):
    k = 0
    for j in range(i, n):
      first = a[k] + matrix[k+1][j][1]
      last = a[j] + matrix[k][j-1][1]
      if first > last:
        matrix[k][j][0] = first
        matrix[k][j][1] = matrix[k+1][j][0]
      else:
        matrix[k][j][0] = last
        matrix[k][j][1] = matrix[k][j-1][0]
      k += 1
  return matrix[0][n-1][0]

a1 = [ 8, 15, 3, 7 ]
a2 = [ 2, 2, 2, 2 ]
a3 = [ 20, 30, 2, 2, 10]
a4 = [18, 20, 15, 30, 10, 14]
print(maxCoinSum(a, len(a)))
print(maxCoinSum(a1, len(a1)))
print(maxCoinSum(a2, len(a2)))
print(maxCoinSum(a3, len(a3)))
print(maxCoinSum(a4, len(a4)))

