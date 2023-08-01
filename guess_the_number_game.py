import math
import random

def printDistanceToTarget(answer, target):
  distance = math.fabs(target - answer)

  if distance >= 10:
    print('It\'s a lot farther than the numbers I set!!')
  elif distance >= 6:
    print('It\'s a little farther than the number I decided on!!')
  else:
    print('It\'s just a little farther than the numbers I\'ve decided on!!')


def showWinOrLoss(win, target):
  if win:
    print()
    print('Is the correct answer!!')
    print('The number I created is ' + str(target) + '!!')
    print('You win!!')
  else:
    print('You loss.(T_T)')
    print('The number I created is ' + str(target) + "!")

  print('Quit the game.')

def startGame(min, max):
  target = random.randint(min,max)

  win = False
  count = 1
  maxCount = math.floor((max - min) / 3)

  if maxCount <= 0:
    maxCount = 1

  print()
  print('You can answer ' + str(maxCount) + ' more times.')

  while count <= maxCount:
    answer = input('Guess between ' + str(min) + ' and ' + str(max) + ' : ')

    if not (str.isdigit(answer)):
      print()
      print('You can only enter positive integers.')
      continue
    elif int(answer) < min:
      print()
      print('That\'s less than ' + str(min) + '.')
      continue
    elif int(answer) > max:
      print()
      print('That\'s greater than ' + str(max) + '.')
    elif int(answer) == target:
      win = True
      break
    else:
      print()
      print('Incorrect.(T_T)')
      printDistanceToTarget(int(answer), target)

    print()
    print('You can answer ' + str(maxCount - count) + ' more times.')
    count += 1

  showWinOrLoss(win, target)

def inputNumber():
  while True:
    print()
    min = input('Please enter the minimum positive integer value : ')
    max = input('Please enter the maximum positive integer value : ')

    if not (str.isdigit(min)) or not (str.isdigit(max)):
      print()
      print('Please enter a valid value!!\n')
    elif int(min) >= int(max):
      print()
      print('The minimum value should be greater than the maximum value!!\n')
    else:
      print()
      print('I will choose a number from ' + min + ' to ' + max + '. Please guess the number I decided.')
      startGame(int(min), int(max))
      break

def checkStartGame():
  print()
  start = input('Do you want to start the game? Y/N : ')
  start = start.upper()

  while True:
    if start == 'Y':
      print()
      print('Start Guess the number game!')
      inputNumber()
      break
    elif start == 'N':
      print()
      print('OK!')
      break
    else:
      print()
      print('Please answer Y or N.')
      break


checkStartGame()
