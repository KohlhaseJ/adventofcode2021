with open("input.txt") as f:
  input = f.readlines()

horizontalPosition = 0
depth = 0

for line in input:
  [direction, steps] = line.split()[0:2]
  steps = int(steps)
  if direction == "forward":
    horizontalPosition += steps
  if direction == "down":
    depth += steps
  if direction == "up":
    depth -= steps

print("Part 1")
print("horizontalPosition {}, depth {}".format(horizontalPosition, depth))
print("Answer {}".format(horizontalPosition * depth))
horizontalPosition = 0
depth = 0
aim = 0

for line in input:
  [direction, steps] = line.split()[0:2]
  steps = int(steps)
  if direction == "forward":
    horizontalPosition += steps
    depth += aim*steps
  if direction == "down":
    aim += steps
  if direction == "up":
    aim -= steps

print("\nPart 2")
print("horizontalPosition {}, depth {}".format(horizontalPosition, depth))
print("Answer {}".format(horizontalPosition * depth))