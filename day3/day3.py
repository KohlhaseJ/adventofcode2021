input = []
with open("input.txt") as f:
  for line in f.readlines():
    input.append([int(i) for i in line.rstrip('\n')])

ones = [i.count(1) for i in zip(*input)]
zeros = [i.count(0) for i in zip(*input)]
zeroMoreCommon = [a > b for a, b in zip(zeros, ones)]

gamma = int("".join(["0" if a else "1" for a in zeroMoreCommon]), 2)
epsilon = int("".join(["1" if a else "0" for a in zeroMoreCommon]), 2)

oxygen = input.copy()
carbon = input.copy()

for i in range(len(input[0])):
  if len(oxygen) > 1:
    ones = [i.count(1) for i in zip(*oxygen)]
    zeros = [i.count(0) for i in zip(*oxygen)]
    zeroMoreCommon = [a > b for a, b in zip(zeros, ones)]
    oxygen = [o for o in oxygen if o[i]==(0 if zeroMoreCommon[i] else 1)]
  if len(carbon) > 1:
    ones = [i.count(1) for i in zip(*carbon)]
    zeros = [i.count(0) for i in zip(*carbon)]
    zeroMoreCommon = [a > b for a, b in zip(zeros, ones)]
    carbon = [o for o in carbon if o[i]==(1 if zeroMoreCommon[i] else 0)]

print(oxygen, carbon)
  
oxygen = int("".join([str(o) for o in oxygen[0]]), 2)
carbon = int("".join([str(o) for o in carbon[0]]), 2)

print("gamma: {}".format(gamma))
print("epsilon: {}".format(epsilon))
print("power consumption: {}".format(gamma*epsilon))
print("oxygen: {}".format(oxygen))
print("carbon: {}".format(carbon))
print("life support rating: {}".format(oxygen*carbon))
exit()