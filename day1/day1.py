with open("c:/dev/adventofcode/day1/input.txt") as f:
  input = f.readlines()

input = list(map(int, input))

timesIncreased = 0 
for i in range(1, len(input)):
  if input[i] > input[i-1]:
    timesIncreased += 1

print("Input increased {} times".format(timesIncreased))

slidingWindowSize = 3
timesIncreased = 0

for i in range(1, len(input)-slidingWindowSize+1):
  A = sum(input[i-1:i+slidingWindowSize-1])
  B = sum(input[i:i+slidingWindowSize])
  if B > A:
    timesIncreased += 1
  
print("Input increased over sliding window (size {}) {} times".format(slidingWindowSize, timesIncreased))
