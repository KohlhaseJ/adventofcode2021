def centerDistance(inputList):
  inputLength = len(inputList)
  if inputLength % 2 == 0:
    y = inputList[inputLength//2]
  else:
    y = (inputList[inputLength//2]+inputList[(inputLength+1)//2])/2
    
  dist = 0
  for i in range(len(crabpositions)):
    dist += abs(crabpositions[i] - y)

  return dist

def computeCost(arr, X):
  cost = 0
  for i in range(len(arr)):
    cost += sum(range(abs(arr[i] - X) + 1))
  return cost

def ternaryMinSearch(arr, left, right, fcost):
  if abs(right - left) <= 2:
    return fcost(arr, (left + right) // 2)
  
  mid1 = left + (right - left) // 3
  mid2 = right - (right - left) // 3

  if fcost(arr, mid1) < fcost(arr, mid2):
      return ternaryMinSearch(arr, left, mid2, fcost)
  else:
      return ternaryMinSearch(arr, mid1, right, fcost)

def binaryMinSearch(arr, left, right, fcost, lastcost):
  if abs(right - left) <= 2:
    return fcost(arr, (left + right) // 2)
  
  mid = left + (right - left) // 2
  currentcost = fcost(arr, mid)

  if currentcost < lastcost:
    return binaryMinSearch(arr, left, mid, fcost, currentcost)
  else:
    return binaryMinSearch(arr, mid, right, fcost, currentcost) 


with open("input.txt") as f:
  crabpositions = [int(i) for i in f.readlines()[0].split(',')]
crabpositions.sort()

cost = centerDistance(crabpositions)
print("Center distance (part 1) {}".format(cost))

cost = binaryMinSearch(crabpositions, crabpositions[0], crabpositions[len(crabpositions)-1], computeCost, 0)
print("Binary searched min cost {}".format(cost))

cost = ternaryMinSearch(crabpositions, crabpositions[0], crabpositions[len(crabpositions)-1], computeCost)
print("Ternary searched min cost {}".format(cost))

