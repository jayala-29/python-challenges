import math

# function descriptor: evalPoly(f,a)
# evaluates a polynomial with the given coefficients
# f - list of numbers, indicates coefficient of respective degree term
# a - number to be evaluated
# return type: number
# example: ([7, -3, 0, 1], 4) => return 59
#          evaluates 7 - 3x + x^3 at x = 4

def evalPoly(f,a):
  output = 0
  for i in range(len(f)): 
    output += a ** i * f[i]
  return output

print(evalPoly([7, -3, 0, 1], 4))
