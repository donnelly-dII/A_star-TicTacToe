import common

class Node:
	def __init__(self, x, y,far, p):
		self.X = x
		self.Y = y
		self.parent = p
		self.cumDistance = far
	def CalcDistance(self, goalX, goalY):
		self.distance = ManDistance(self.X,self.Y, goalX,goalY)
		self.cost = self.distance + self.cumDistance

def findPoint(map, goal):
	xx = 0
	yy = 0
	while(xx < common.constants.MAP_WIDTH):
		yy = 0
		while(yy < common.constants.MAP_HEIGHT):
			if map[yy][xx] == goal:
				return xx, yy
			yy = yy + 1
		xx = xx + 1

def HashMap(n,m):
	a = []
	for i in range(n):
		a.append([False] * m)
	return a

def ManDistance(currX, currY, goalX, goalY):
	retX = goalX - currX
	retY = goalY - currY
	if retX < 0:
		retX = retX * -1
	if retY < 0:
		retY = retY*-1
	return retX + retY

def GetMinNode(inputList):
	if not inputList:
		return None
	minHold = 0
	minNode = inputList[0]
	for ii in range(0,len(inputList)):
		if inputList[ii].cost < minNode.cost:
			minHold = ii
			minNode = inputList[ii]
		elif inputList[ii].cost == minNode.cost:
			if inputList[ii].X < minNode.X:
				minHold = ii
				minNode = inputList[ii]
			elif inputList[ii].X == minNode.X:
				if inputList[ii].Y < minNode.Y:
					minNode = inputList[ii]
					minHold = ii
	return minHold

def TraceBack(map, end):
	currNode = end
	while currNode != None:
		map[currNode.Y][currNode.X] = 5
		currNode = currNode.parent

def astar_search(map):
   	found = False
   	xStart, yStart = findPoint(map, 2)
   	xGoal, yGoal = findPoint(map,3)
   	VisitedMap = HashMap(common.constants.MAP_HEIGHT, common.constants.MAP_WIDTH)
   	OpenList = []
   	firstNode = Node(xStart, yStart, 0, None)
   	firstNode.CalcDistance(xGoal, yGoal)
   	OpenList.append(firstNode)
   	count = 0
   	while len(OpenList)!=0  and not found:
   		currindex = GetMinNode(OpenList)
   		currNode = OpenList[currindex]
   		xHold = currNode.X 
   		yHold = currNode.Y
   		if map[yHold][xHold] == 3:
   			map[yHold][xHold] = 4
   			finalNode = currNode
   			found = True
   			break
   		map[yHold][xHold] = 4
   		if VisitedMap[yHold][xHold] != True and not found:
   			VisitedMap[yHold][xHold] = True
   			if xHold + 1 < common.constants.MAP_WIDTH and map[yHold][xHold+1]!=1 and not VisitedMap[yHold][xHold+1]:
   				newNode = Node(xHold+1,yHold,currNode.cumDistance + 1,currNode)
   				newNode.CalcDistance(xGoal, yGoal)
   				OpenList.append(newNode)
   			if yHold + 1 < common.constants.MAP_HEIGHT and map[yHold + 1][xHold]!=1 and not VisitedMap[yHold+1][xHold]:
   				newNode = Node(xHold, yHold+1,currNode.cumDistance+1,currNode)
   				newNode.CalcDistance(xGoal, yGoal)
   				OpenList.append(newNode)
   			if xHold-1>=0 and map[yHold][xHold-1]!=1 and not VisitedMap[yHold][xHold-1]:
   				newNode = Node(xHold-1,yHold,currNode.cumDistance + 1, currNode)
   				newNode.CalcDistance(xGoal,yGoal)
   				OpenList.append(newNode)
   			if yHold-1>=0 and map[yHold-1][xHold]!=1 and not VisitedMap[yHold-1][xHold]:
   				newNode=Node(xHold,yHold-1,currNode.cumDistance+1,currNode)
   				newNode.CalcDistance(xGoal,yGoal)
   				OpenList.append(newNode)
   		OpenList.pop(currindex)
   	if found:
   		TraceBack(map,finalNode)
   	return found










