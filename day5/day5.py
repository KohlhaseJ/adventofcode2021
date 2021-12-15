lines = []
with open("input.txt") as f:
  for line in f.readlines():
    lines.append([int(n) for point in line.rstrip('\n').split(' -> ') for n in point.split(',')])

maxXY = max([max(idx) for idx in zip(*lines)])

matrix = [[0 for _ in range(maxXY+1)] for _ in range(maxXY+1)]


for line in lines:
  x1, y1, x2, y2 = line
  if x1 == x2 or y1 == y2:
    for x in range(min(x1,x2), max(x1,x2)+1):
      for y in range(min(y1,y2), max(y1,y2)+1):
        matrix[y][x] += 1
  else:
    xi = 1 if x2>x1 else -1
    yi = 1 if y2>y1 else -1
    for x,y in zip(range(x1, x2 + xi, xi), range(y1, y2 + yi, yi)):
      matrix[y][x] += 1

result = sum([1 if x > 1 else 0 for row in matrix for x in row])
print("Number of intersection points: {}".format(result))
