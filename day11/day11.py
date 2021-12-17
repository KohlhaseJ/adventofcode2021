def getAdjacents(x, y, lenX, lenY):
  adjacents = [(x-1, y), (x-1, y-1), (x-1, y+1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1)]
  filtered = [(x, y) for (x , y) in adjacents if x >= 0 and x < lenX and y >= 0 and y < lenY]
  return filtered

def updateEnergy(map, flashed, x, y):
  if (x, y) not in flashed:
    map[x][y] += 1

  if map[x][y] > 9:
    flashed.append((x, y))
    map[x][y] = 0
    for ax, ay in getAdjacents(x,y, len(map), len(map[0])):
      updateEnergy(map, flashed, ax, ay)

map = []
with open("input.txt") as f:
  for line in f.readlines():
    map.append([int(x) for x in line.rstrip('\n')])

numberOfSteps = 100
sumOfFlashes = 0

for _ in range(numberOfSteps):
  flashed = []
  for x in range (len(map)):
    for y in range(len(map[0])):
      updateEnergy(map,flashed, x, y)
  sumOfFlashes += len(flashed)

stepCounter = numberOfSteps
allFlashed = False
while not allFlashed:
  stepCounter += 1
  flashed = []
  for x in range (len(map)):
    for y in range(len(map[0])):
      updateEnergy(map,flashed, x, y)
  
  if sum([x for line in map for x in line]) == 0:
    allFlashed = True

print("How many total flashes are there after 100 steps?: {}".format(sumOfFlashes))
print("What is the first step during which all octopuses flash?: {}".format(stepCounter))