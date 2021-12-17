def rotateMatrix(m):
  return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def flipMatrix(m):
  flipped = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
  for i in range(len(m)):
    for j in range(len(m[0])):
      flipped[i][len(m[0])-1-j] = m[i][j]
  return flipped

def joinMatrices(A, B):
  joined = [[0 for _ in range(max(len(A[0]), len(B[0])))] for _ in range(max(len(A), len(B)))]
  for i in range(len(joined)):
    for j in range(len(joined[0])):
      valueA = 0 if i >= len(A) or j >= len(A[0]) else A[i][j]
      valueB = 0 if i >= len(B) or j >= len(B[0]) else B[i][j]
      joined[i][j] = max(valueA, valueB)
  return joined

def printMatrix(m):
  for line in m:
    print(line)
  print('')

dots = []
instructions = []
isPaperLine = True
with open("input.txt") as f:
  for line in f.readlines():
    line = line.rstrip('\n')
    if line == "":
      isPaperLine = False
      continue

    if isPaperLine:
      dots.append([int(x) for x in line.split(',')])
    else:
      instructions.append(line.lstrip('fold along ').split('='))

paper = [[0 for _ in range(max([xy[0] for xy in dots])+1)] for _ in range(max([xy[1] for xy in dots])+1)]
for xy in dots:
  paper[xy[1]][xy[0]] = 1

folded = paper.copy()
for instruction in instructions:
  foldOver = instruction[0]
  foldAt = int(instruction[1])
  if foldOver == 'y':
    left = folded[0:foldAt]
    right = folded[foldAt+1:len(folded)]
    left = rotateMatrix(left)
    right = rotateMatrix(right)
    left = flipMatrix(left)
    folded = joinMatrices(left, right)
    folded = flipMatrix(folded)
    folded = rotateMatrix(rotateMatrix(rotateMatrix(folded)))
  if foldOver == 'x':
    rotated = rotateMatrix(rotateMatrix(rotateMatrix(folded)))
    left = rotated[0:foldAt]
    right = rotated[foldAt+1:len(rotated)]
    left = rotateMatrix(left)
    right = rotateMatrix(right)
    left = flipMatrix(left)
    folded = joinMatrices(left, right)
    folded = flipMatrix(folded)


  print(sum([x for line in folded for x in line]))

printMatrix(folded)