from Modules.mainTestModule01 import main as main01, cube as cube01, moveList as moveList01
from Modules.mainTestsModule02 import main as main02, cube as cube02, moveList as moveList02
from Modules.mainTestsModule03 import main as main03, cube as cube03, moveList as moveList03
from Modules.mainTestsModule04 import main as main04, cube as cube04, moveList as moveList04
from Modules.mainTestsModule05 import main as main05, cube as cube05, moveList as moveList05
from Modules.mainTestsModule06 import main as main06, cube as cube06, moveList as moveList06
from multiprocessing import Process, Manager
import time

def parallel_execution01(mainList01):
    curTime = time.time()
    mainList01.extend(main01(cube01, moveList01))
    print("Время выполнения parallel_execution01:", time.time() - curTime)

def parallel_execution02(mainList02):
    curTime = time.time()
    mainList02.extend(main02(cube02, moveList02))
    print("Время выполнения parallel_execution02:", time.time() - curTime)

def parallel_execution03(mainList03):
    curTime = time.time()
    mainList03.extend(main03(cube03, moveList03))
    print("Время выполнения parallel_execution03:", time.time() - curTime)

def parallel_execution04(mainList04):
    curTime = time.time()
    mainList04.extend(main04(cube04, moveList04))
    print("Время выполнения parallel_execution04:", time.time() - curTime)

def parallel_execution05(mainList05):
    curTime = time.time()
    mainList05.extend(main05(cube05, moveList05))
    print("Время выполнения parallel_execution05:", time.time() - curTime)

def parallel_execution06(mainList06):
    curTime = time.time()
    mainList06.extend(main06(cube06, moveList06))
    print("Время выполнения parallel_execution06:", time.time() - curTime)

if __name__ == "__main__":
    with Manager() as manager:
        mainList01 = manager.list()
        mainList02 = manager.list()
        mainList03 = manager.list()
        mainList04 = manager.list()
        mainList05 = manager.list()
        mainList06 = manager.list()

        thread01 = Process(target=parallel_execution01, args=(mainList01,))
        thread02 = Process(target=parallel_execution02, args=(mainList02,))
        thread03 = Process(target=parallel_execution03, args=(mainList03,))
        thread04 = Process(target=parallel_execution04, args=(mainList04,))
        thread05 = Process(target=parallel_execution05, args=(mainList05,))
        thread06 = Process(target=parallel_execution06, args=(mainList06,))

        thread01.start()
        thread02.start()
        thread03.start()
        thread04.start()
        thread05.start()
        thread06.start()

        thread01.join()
        thread02.join()
        thread03.join()
        thread04.join()
        thread05.join()
        thread06.join()

        mainList = []
        mainList.extend(mainList01)
        mainList.extend(mainList02)
        mainList.extend(mainList03)
        mainList.extend(mainList04)
        mainList.extend(mainList05)
        mainList.extend(mainList06)

        with open('nonSortedMatrixresult.txt', 'w') as file:
            for i in mainList:
                file.write(f'{i[0]} -> {i[1]}\n')
        file.close()

        mainList = sorted(mainList, key=lambda x: x[1], reverse=False)

        with open('sortedMatrixresult.txt', 'w') as file1:
            for i in mainList:
                file1.write(f'{i[0]} -> {i[1]}\n')
        file1.close()