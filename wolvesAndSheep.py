def wolvesAndSheep(n,w,s): 
  b = [[0 for i in range(n)]for j in range(n)]
  for i in range(n): 
    l = []
    for j in range(n): 
      if([i,j] in w): 
        b[i][j] = "W"
      else: 
        if([i,j] in s): 
          b[i][j] = "S"
        else: 
          b[i][j] = "_"
      l.append(b[i][j] + " ")
    print("".join(l))
  board = [[0 for i in range(n)]for j in range(n)]
  for wolf in w: 
    row = wolf[0]
    col = wolf[1]
    # rows
    for c in range(n): 
      board[row][c] = 1
    # columns
    for r in range(n): 
      board[r][col] = 1
    r = row
    c = col
    # right bottom diagonal 
    while True: 
      r += 1
      c += 1
      if(r < n and c < n): 
        board[r][c] = 1
      else: 
        r = row
        c = col
        break
    # left bottom diagonal 
    while True: 
      r += 1
      c -= 1
      if(r < n and c >= 0): 
        board[r][c] = 1
      else: 
        r = row
        c = col
        break
    # left top diagonal 
    while True: 
      r -= 1
      c -= 1
      if(r >= 0 and c >= 0): 
        board[r][c] = 1
      else: 
        r = row
        c = col
        break
    # right top diagonal 
    while True: 
      r -= 1
      c += 1
      if(r >= 0 and c < n): 
        board[r][c] = 1
      else: 
        break
  for i in range(n): 
    l = []
    for j in range(n): 
      l.append(str(board[i][j]) + " ")
    print("".join(l))
  count = 0
  for sheep in s: 
    if(board[sheep[0]][sheep[1]] == 1): 
      print("Your sheep at row " + str(sheep[0]+1) + ", column " + str(sheep[1]+1) + " is in DANGER.")
      count += 1
  if(count == 0): 
    if len(s) == 1: 
      print("Your sheep is safe! >o<")
    else: 
      print("Your sheep are safe! >o<")
  return 

wolvesAndSheep(10,[[1,0],[3,4]],[[2,3],[7,9]])
