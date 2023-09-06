# 0: 'White', 1: 'Yellow', 2: 'Orange', 3: 'Red', 4: 'Green', 5: 'Blue' blueUp
import magiccube

cube = magiccube.Cube(3,"YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

print(
    'R().except(4)\nR()U()Rb()Ub().exept(6)\nRu().exept(126) \n U()L()U()R().except(480)'
)

answer = 0

params = ["U", "U'", "R", "R'", "L", "L'", "B", "B'", "F", "F'", "D", "D'"]

moveList = str(
    input(
        ' u - rotate upper side to left \n ub - rotate upper side to right \n r - rotate right side to up \n rb rotate right side to down \n l - rotate left side to up \n lb - rotate left side to down \n b - rotate back side to right \n bb - rotate back side to left \n f - rotate front side to right \n fb - rotate front side to left \n Example: r u rb ub \n Write form: '
    )).upper()


def start(steps):
  global answer
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
      print(cube)
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
  steps = validateInputs(clearInputs(moves.split(' ')))
  start(steps)
  print(cube)
  print(answer)


main(moveList)

input()
