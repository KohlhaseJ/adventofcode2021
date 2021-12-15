def computeCost(arr, X):
  cost = 0
  for i in range(len(arr)):
    cost += abs(arr[i] - X)
  return cost

def computeTriangularCost(arr, X):
  cost = 0
  for i in range(len(arr)):
    cost += sum(range(abs(arr[i] - X) + 1))
  return cost
  
def centerDistance(inputList, fdist):
  inputLength = len(inputList)
  if inputLength % 2 == 0:
    y = inputList[inputLength//2]
  else:
    y = (inputList[inputLength//2]+inputList[(inputLength+1)//2])/2

  return fdist(crabpositions, y)

def ternaryMinSearch(arr, left, right, fcost):
  if abs(right - left) <= 2:
    return fcost(arr, (left + right) // 2)
  
  mid1 = left + (right - left) // 3
  mid2 = right - (right - left) // 3

  if fcost(arr, mid1) < fcost(arr, mid2):
      return ternaryMinSearch(arr, left, mid2, fcost)
  else:
      return ternaryMinSearch(arr, mid1, right, fcost)


with open("input.txt") as f:
  crabpositions = [int(i) for i in f.readlines()[0].split(',')]
crabpositions.sort()

print("Part 1: center distance: {}".format(centerDistance(crabpositions, computeCost)))
print("Part 1: ternary searched min cost: {}".format(ternaryMinSearch(crabpositions, crabpositions[0], crabpositions[len(crabpositions)-1], computeCost)))

print("Part 2: center distance: {}".format(centerDistance(crabpositions, computeTriangularCost)))
print("Part 2: ternary searched min cost: {}".format(ternaryMinSearch(crabpositions, crabpositions[0], crabpositions[len(crabpositions)-1], computeTriangularCost)))
