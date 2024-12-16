input = open("./input.txt")
guardMap = list(map(list, map(str.strip, input.readlines())))

def is_valid(x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

def countRoad(inputMap):
    rows = len(inputMap)
    cols = len(inputMap[0])
    direction = 0
    directionMap = {
          0: (-1, 0),
          1: (0, 1),
          2: (1, 0),
          3: (0, -1)
    }
    visited = []
    exit = False

    for i in range(rows):
          for j in range(cols):
                if inputMap[i][j] == "^":
                      position_i = i
                      position_j = j
                      while True:
                            new_i = position_i + directionMap[direction][0]
                            new_j = position_j + directionMap[direction][1]
                            if is_valid(new_i, new_j, rows, cols):
                                if inputMap[new_i][new_j] == "#":
                                    if [position_i, position_j] not in visited:
                                        visited.append([position_i, position_j])
                                    direction = (direction + 1) % 4
                                    position_i += directionMap[direction][0]
                                    position_j += directionMap[direction][1]
                                else:
                                    if [position_i, position_j] not in visited:
                                        visited.append([position_i, position_j])
                                    position_i = new_i
                                    position_j = new_j
                            else:
                                  visited.append([position_i, position_j])
                                  exit = True
                                  break
                if exit:
                      break
    return len(visited)

def checkLoop(inputMap, rows, cols):
    visited = set()
    direction_i, direction_j = -1, 0

    for i in range(rows):
          for j in range(cols):
               if inputMap[i][j] == "^":
                    start_i, start_j = i, j
    current_i, current_j = start_i, start_j
    
    while True:
        if (current_i, current_j, direction_i, direction_j) in visited:
             return True
        visited.add((current_i, current_j, direction_i, direction_j))
        if not is_valid(current_i+direction_i, current_j+direction_j, rows, cols):
             return False
        if guardMap[current_i + direction_i][current_j + direction_j] == "#":
             direction_j, direction_i = -direction_i, direction_j
        else:
             current_i += direction_i
             current_j += direction_j

def findLoop(inputMap):
    rows = len(inputMap)
    cols = len(inputMap[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if inputMap[i][j] != ".":
                continue
            inputMap[i][j] = "#"
            if checkLoop(inputMap, rows, cols):
                count += 1
            inputMap[i][j] = "."
    return count
     
    
count = countRoad(guardMap)
loops = findLoop(guardMap)
print(count)
print(loops)
