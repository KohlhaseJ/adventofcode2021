with open("input.txt") as f:
  lines = [line.rstrip('\n') for line in f.readlines()]

template = lines[0]
pairInsertions = {}
for line in lines[2:len(lines)]:
  key, value = line.split(' -> ')
  pairInsertions[key] = value

steps = 40
pairs = {}
for i in range(len(template) - 1):
  pairs[template[i:i+2]] = 1

for _ in range(steps):
  temp = list(pairs.keys()).copy()
  for pair in temp:
    insertion = pairInsertions[pair]
    pairA = pair[0] + insertion
    pairB = insertion + pair[1]

    if pairA in pairs:
      pairs[pairA] += 1
    else:
      pairs[pairA] = 1
    if pairB in pairs:
      pairs[pairB] += 1
    else:
      pairs[pairB] = 1
      


print(pairs)