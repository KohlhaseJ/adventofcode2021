def boardWon(marker):
  hasCompleteRow = 5 in [sum(r) for r in marker]
  hasCompleteCol = 5 in [sum(c) for c in zip(*marker)]
  return hasCompleteRow or hasCompleteCol

def markNumbers(board, marker, number):
  for i, row in enumerate(board):
    for j, value in enumerate(row):
      if value == number:
        marker[i][j] = 1

def getFirstWinner(boards, markers, numbers):
  for number in numbers:
    for board, marker in zip(boards, markers):
      markNumbers(board, marker, number)
      if boardWon(marker):
        return(board, marker, number)

def getLastWinner(boards, markers, numbers):
  for number in numbers:
    bi = 0
    while len(boards) > 0 and bi < len(boards):
      markNumbers(boards[bi], markers[bi], number)
      if boardWon(markers[bi]):
        lastWinner = (boards.pop(bi), markers.pop(bi), number)
      else:
        bi += 1
  return lastWinner

def calculateResult(board, marker, number):
  flat_board = [item for row in board for item in row]
  flat_marker = [item for row in marker for item in row]
  result = sum([value if bit == 0 else 0 for value, bit in zip(flat_board, flat_marker)])*number
  return result

with open("c:/dev/adventofcode/day4/input.txt") as f:
  for i, line in enumerate(f.readlines()):
    if i == 0:
      numbers = [int(n) for n in line.rstrip('\n').split(',')]
      currentBoard = []
      boards = []
    elif i > 1:
      if line.rstrip('\n') == '':
        boards.append(currentBoard)
        currentBoard = []
      else:
        currentBoard.append([int(n) for n in line.lstrip(' ').rstrip('\n').replace('  ', ' ').split(' ')])

markers = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
board, marker, number = getFirstWinner(boards, markers, numbers)
print('-----------------------------')
print('First winning board: {}'.format(board))
print('with marker: {}'.format(marker))
print('for number: {}'.format(number))
print('-----------------------------')
print('results in: {}'.format(calculateResult(board, marker, number)))
print('-----------------------------')
print('')
print('-----------------------------')
markers = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
board, marker, number = getLastWinner(boards, markers, numbers)
print('Last winning board: {}'.format(board))
print('with marker: {}'.format(marker))
print('for number: {}'.format(number))
print('-----------------------------')
print('results in: {}'.format(calculateResult(board, marker, number)))
print('-----------------------------')