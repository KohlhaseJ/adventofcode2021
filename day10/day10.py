legalPairs = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

illegalCharacterScores = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

completedCharacterScores = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

def isLegalPair(opensWith, closesWith):
  return legalPairs.get(opensWith, 'invalid') == closesWith

def isOpeningBracket(character):
  return character in ['(', '[', '{', '<']

def isClosingBracket(character):
  return character in [')', ']', '}', '>']

def getMiddleElement(list):
  return list[len(list)//2]

with open("input.txt") as f:
  lines = [line.rstrip('\n') for line in f.readlines()]

syntaxErrorScore = 0
autocompletionScores = []

for line in lines:
  openingCharacters = []
  autocompletionScore = 0
  isIncompleteLine = True
  for character in line:
    if isOpeningBracket(character):
      openingCharacters.append(character)
    elif isClosingBracket(character):
      lastOpeningCharacter = openingCharacters.pop()
      if not isLegalPair(lastOpeningCharacter, character):
        print("Syntax error: expected {} got {}!".format(legalPairs.get(lastOpeningCharacter), character))
        syntaxErrorScore += illegalCharacterScores.get(character, 0)
        isIncompleteLine = False
        break

  if isIncompleteLine:
    while len(openingCharacters) > 0:
      autocompletionCharacter = legalPairs.get(openingCharacters.pop())
      autocompletionScore *= 5
      autocompletionScore += completedCharacterScores.get(autocompletionCharacter, 0)
      line += autocompletionCharacter

    if autocompletionScore > 0:
      autocompletionScores.append(autocompletionScore)

autocompletionScores.sort()

print("What is the total syntax error score?: {}".format(syntaxErrorScore))
print("What is the middle score?: {}".format(getMiddleElement(autocompletionScores)))