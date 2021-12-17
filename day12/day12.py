
connections = {}
with open("input.txt") as f:
  for line in [line.rstrip('\n') for line in f.readlines()]:
    connection = line.split('-')
    nodeA = connection[0]
    nodeB = connection[1]

    if nodeA in connections:
      connections[nodeA].append(nodeB)
    else:
      connections[nodeA] = [nodeB]
    
    if nodeB in connections:
      connections[nodeB].append(nodeA)
    else:
      connections[nodeB] = [nodeA]

paths = []
def findPath(start, end, lastPath):
  for connectedNode in connections[start]:
    currentPath = lastPath.copy()
    if connectedNode == 'start':
      continue
    
    visitedSmallCaves = [node for node in currentPath if node.islower()]
    visitedSmallCaveTwice = len(visitedSmallCaves) != len(set(visitedSmallCaves))
    if connectedNode in currentPath and connectedNode.islower() and visitedSmallCaveTwice:
      continue

    currentPath.append(connectedNode)
    if connectedNode == end:
      paths.append(currentPath)
    else:
      findPath(connectedNode, end, currentPath.copy())

findPath('start', 'end', ['start'])

print(len(paths))