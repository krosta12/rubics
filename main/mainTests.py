import magiccube

cube = magiccube.Cube(3,"YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

print(
    "R().except(4)\nR()U()R()U'().exept(6)\nR()U().exept(126) \n U()L()U()R().except(480)"
)

answer = 0

params = ["U", "U'", "R", "R'", "L", "L'", "B", "B'", "F", "F'", "D", "D'"]

moveList = str(
    input(
        " u - rotate upper side to left \n u - rotate upper side to right \n r - rotate right side to up \n r' rotate right side to down \n l - rotate left side to up \n l' - rotate left side to down \n b - rotate back side to right \n b' - rotate back side to left \n f - rotate front side to right \n f' - rotate front side to left \n Example: r u r' u' \n Write form: "
    )).upper()


def start(steps):
  global answer
  answer=0
  isStarted = False
  consoleRequest = ''
  print(steps)
  for i in steps:
    consoleRequest += f'{i}  '
  while cube.is_done() == False or isStarted == False:
    isStarted = True
    for i in consoleRequest.split():
      answer += 1
      request = f'cube.rotate("{i}")'
      eval(request)
      


def clearInputs(inputs):
  for i in inputs:
    if i == '':
      inputs.remove(i)
  inputs = validateInputs(inputs)
  return inputs


def validateInputs(validate):
  for i in validate:
    if i in params:
      pass
    else:
      validate.remove(i)
  return validate


def main(moves):
  testlist = ['','']
  fullyList = []
  for i in range(len(params)):
    testlist[0] = params[i]
    for i2 in range(len(params)):
      testlist[1] = params[i2]
      start(testlist)
      # print(answer)
      fullyList.append([testlist.copy(), answer])
  sortedList = sorted(fullyList, key=lambda x: x[1], reverse=False)

  for i in sortedList:
    with open('matrixresult.txt', 'a') as file:
      file.write(f'{i[0]} -> {i[1]}\n')
  print(sortedList)

main(moveList)
input()
