inputValues = []
outputValues = []

with open("input.txt") as f:
  for line in f.readlines():
    line = line.rstrip('\n')
    inputValues.append([i for i in line.split(' | ')[0].split(' ')])
    outputValues.append([i for i in line.split(' | ')[1].split(' ')])


sum = 0

for input, output in zip(inputValues, outputValues):
  # 7-segment
  #     A
  #  B     C
  #     D
  #  E     F
  #     G

  # fix codes from length
  CF = [c for x in input if len(x) == 2 for c in x]
  ACF = [c for x in input if len(x) == 3 for c in x]
  BCDF = [c for x in input if len(x) == 4 for c in x]
  ABCDEFG = [c for x in input if len(x) == 7 for c in x]

  # find encoding
  A = list(set(ACF) - set(CF))
  BD = list(set(BCDF) - set(CF))
  EG = list(set(ABCDEFG) - set(A) - set(BD) - set(CF))
  
  ABFG = ABCDEFG.copy()
  for encoding in [x for x in input if len(x) == 6]:
    ABFG = list(set(ABFG).intersection(set(encoding)))
  CDE = list(set(ABCDEFG) - set(ABFG))

  B = list(set(BD) - set(CDE))
  F = list(set(CF) - set(CDE))
  G = list(set(EG) - set(CDE))
  D = list(set(BD) - set(B))
  C = list(set(CF) - set(F))
  E = list(set(EG) - set(G))
  
  # set remaining codes
  codes = []
  codes.append(A+B+C+E+F+G)   # 0
  codes.append(C+F)           # 1
  codes.append(A+C+D+E+G)     # 2
  codes.append(A+C+D+F+G)     # 3
  codes.append(B+C+D+F)       # 4
  codes.append(A+B+D+F+G)     # 5
  codes.append(A+B+D+E+F+G)   # 6
  codes.append(A+C+F)         # 7
  codes.append(A+B+C+D+E+F+G) # 8
  codes.append(A+B+C+D+F+G)   # 9

  # decode output
  strNum = ''
  for encoding in output:
    match = [i for i,x in enumerate(codes) if set(x) == set([e for e in encoding])]
    strNum += str(match[0])

  sum += int(strNum)

print("Sum of decoded numbers: {}".format(sum))
