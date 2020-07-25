def invMatrix(m): 
  output = [[0 for i in range(2)] for j in range(2)]
  det = m[0][0]*m[1][1]-m[0][1]*m[1][0]
  if(det == 0): 
    return("Inverse does not exist.")
  output[0][0] = m[1][1]
  output[1][1] = m[0][0]
  output[0][1] = -m[0][1]
  output[1][0] = -m[1][0]
  for i in range(2): 
    for j in range(2): 
      output[i][j] /= det
  return str(output[0][0]) + " " + str(output[0][1]) + "\n" + str(output[1][0]) + " " + str(output[1][1])

print(invMatrix([[4,7],[2,6]]))
