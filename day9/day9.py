def traverseBaisin(map, baisin, x, y):
  adjacents = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
  for ax, ay in adjacents:
    if map[ax][ay] < 9 and (ax, ay) not in baisin:
      baisin.append((ax, ay))
      traverseBaisin(map, baisin, ax, ay)

map = []
with open("input.txt") as f:
  for line in f.readlines():
    elems = [int(x) for x in line.rstrip('\n')]
    elems.insert(0, 10)
    elems.append(10)
    map.append(elems)

map.insert(0, [10 for _ in range(len(map[0]))])
map.append([10 for _ in range(len(map[0]))])

lowpoints = []
basinSizes = []

for x in range (1, len(map) - 1):
  for y in range(1, len(map[0]) - 1):
    value = map[x][y]
    adjacentValues = [map[x-1][y], map[x][y-1], map[x+1][y], map[x][y+1]]
    if all(value < x for x in adjacentValues):
      lowpoints.append(value)
      baisin = [(x,y)]
      traverseBaisin(map, baisin, x, y)
      basinSizes.append(len(baisin))

basinSizes.sort(reverse=True)

print("risk level: {}".format(sum([1 + i for i in lowpoints])))
print("product of three largest baisins: {}".format(basinSizes[0]*basinSizes[1]*basinSizes[2]))