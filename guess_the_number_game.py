import math
import random


def printDistanceToTarget(answer, target):
    distance = math.fabs(target - answer)

    if distance >= 10:
        print("はるかに遠いです!!")
    elif distance >= 4:
        print("ちょっと遠いです!!")
    else:
        print("あと少しです!!")


def showWinOrLoss(win, target):
    if win:
        print()
        print("正解です!!")
        print("私が決めた数字は " + str(target) + " です!!")
        print("あなたの勝ちです!!")
    else:
        print("あなたの負けです(T_T)")
        print("私が決めた数字は " + str(target) + " でした!!")

    while True:
        print()
        again = input("もう一度遊びますか? Y/N : ")
        again = again.upper()

        if again == "Y":
            print()
            print("再開します!!")
            inputNumber()
            break
        elif again == "N":
            print()
            print("了解しました!!")
            print("さようなら!!")
            break
        else:
            print()
            print("Y か N を押してください。")
            continue


def startGame(min, max):
    target = random.randint(min, max)

    win = False
    count = 1
    maxCount = math.floor((max - min) / 3)

    if maxCount <= 0:
        maxCount = 1

    print()
    print("あと " + str(maxCount) + " 回回答出来ます。")

    while count <= maxCount:
        answer = input(str(min) + " から " + str(max) + " の中から推測してください!! : ")

        if not (str.isdigit(answer)):
            print()
            print("整数のみ入力できます。")
            continue
        elif int(answer) < min:
            print()
            print("その値は" + min + "未満です。")
            continue
        elif int(answer) > max:
            print()
            print("その値は " + max + " より大きいです。")
            continue
        elif int(answer) == target:
            win = True
            break
        else:
            print()
            print("不正解(T_T)")
            printDistanceToTarget(int(answer), target)

        rest = maxCount - count
        print()
        if (rest > 0):
            print("あと " + str(rest) + " 回回答出来ます。")
        count += 1

    showWinOrLoss(win, target)


def inputNumber():
    while True:
        print()
        min = input("最小の正の整数値を決定して下さい : ")
        max = input("最大の正の整数値を決定して下さい : ")

        if not (str.isdigit(min)) or not (str.isdigit(max)):
            print()
            print("有効な値を入力してください!!\n")
        elif int(min) >= int(max):
            print()
            print("最小値は最大値より大きくなければなりません!!\n")
        else:
            print()
            print(
                str(min) + " から " + str(max) + " の間でランダムに数字を選びます。"
                + "私が決めた数字を当ててください!!"
            )
            startGame(int(min), int(max))
            break


def checkStartGame():
    while True:
        print()
        start = input("ゲームを始めますか? Y/N : ")
        start = start.upper()

        if start == "Y":
            print()
            print("Guess the number game を始めます!!")
            inputNumber()
            break
        elif start == "N":
            print()
            print("了解しました。")
            break
        else:
            print()
            print("Y か N を入力してください。")
            continue


checkStartGame()
