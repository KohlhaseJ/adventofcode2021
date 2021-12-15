lanternsCount = [0 for _ in range(9)]

with open("c:/dev/adventofcode/day6/input.txt") as f:
  for i in f.readlines()[0].split(','):
    lanternsCount[int(i)] += 1

print("There are {} lantern fish on the first day".format(sum(lanternsCount)))
days = 256

for _ in range(days):
  reproducers = lanternsCount[0]

  for li in range(1, len(lanternsCount)):
    lanternsCount[li-1] = lanternsCount[li]

  lanternsCount[6] += reproducers
  lanternsCount[8] = reproducers

print("There are {} lantern fish after {} days".format(sum(lanternsCount), days))