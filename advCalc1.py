# function descriptor: advCalc1()
# advanced calculator that supports addition and subtraction
# note: input from user does NOT use spaces
#       part 1 of building PEMDAS-based calculator
#       this represents parsing an expression as an algorithm
#       for addition and subtraction, we go "left to right"
#       the example should be parsed as follows:
#           3+7-4+1  <- input
#           10-4+1
#           6+1
#           7        <- output
# return type: nothing; program should end when the user types 'n'
# example: Please enter an expression to calculate: '3+7-4+1'
#          Okay, the output is 7
#          Do you want to calculate anything else? [y|n] 'n'
#          Okay, bye bye :)
def advCalc1():
  while True: 
    expression = input("Please enter and expression to calculate: ")
    ls = []
    numLs = []
    oprLs = []
    current = 0
    lastNum = []
    for item in expression: 
      ls.append(item)
    for i in range(len(ls)): 
      if(ls[i] == "+" or ls[i] == "-"): 
        oprLs.append(ls[i])
        num = []
        lastOpr = i
        for j in range(current,i): 
          num.append(ls[j])
        numLs.append("".join(num))
        current = i+1
    for i in range(lastOpr+1, len(ls)): 
      lastNum.append(ls[i])
    numLs.append("".join(lastNum))
    outcome = int(numLs[0])
    for i in range(len(oprLs)): 
      if(oprLs[i] == "+"): 
        outcome = add(outcome, int(numLs[i+1]))
      if(oprLs[i] == "-"): 
        outcome = sub(outcome, int(numLs[i+1]))
    print("Okay, the output is " + str(outcome))
    more = input("Do you want to calculate anything else? [y|n] ")
    if(more == "n"): 
      print("Okay, bye bye :)")
      break
  return
  
def add(a,b):
  return a + b
  
def sub(a,b):
  return a - b

advCalc()
