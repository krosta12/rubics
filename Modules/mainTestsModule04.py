import magiccube

cube = magiccube.Cube(3,"YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

params = ["U", "U'", "R", "R'", "L", "L'", "B", "B'", "F", "F'", "D", "D'"]
moveList = 'U'
def start(cube, steps):
  answer=0
  isStarted = False
  consoleRequest = ''
  for i in steps:
    consoleRequest += f'{i}  '
  while cube.is_done() == False or isStarted == False:
    isStarted = True
    for i in consoleRequest.split():
      answer += 1
      cube.rotate(i)
  return answer

def main(cube, moves):
  fullyList = []
  for i in range(3,len(params),6):
    for i2 in range(0, len(params)):
      answer = start(cube, [params[i], params[i2]])
      fullyList.append([[params[i], params[i2]], answer])

  for i in range(3,len(params),6):
    for i2 in range(0,len(params)):
      for i3 in range(0,len(params)):
        answer = start(cube, [params[i], params[i2], params[i3]])
        fullyList.append([[params[i], params[i2], params[i3]], answer])

  for i in range(3,len(params),6):
    for i2 in range(0,len(params)):
      for i3 in range(0,len(params)):
        for i4 in range(0,len(params)):
          answer = start(cube, [params[i], params[i2], params[i3], params[i4]])
          fullyList.append([[params[i], params[i2], params[i3], params[i4]], answer])
    
  for i in range(3,len(params),6):
    for i2 in range(0,len(params)):
      for i3 in range(0,len(params)):
        for i4 in range(0,len(params)):
          for i5 in range(0, len(params)):
            answer = start(cube, [params[i], params[i2], params[i3], params[i4], params[i5]])
            fullyList.append([[params[i], params[i2], params[i3], params[i4], params[i5]], answer])
  
  sortedList = sorted(fullyList, key=lambda x: x[1], reverse=False)
  return sortedList