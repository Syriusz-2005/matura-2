def willAdaWin(stonesCount=4):
    if stonesCount == 1: return True
    if stonesCount == 2: return False
    if stonesCount == 3: return True
    if stonesCount == 4: return True

    if willAdaWin(stonesCount - 1) is True or willAdaWin(stonesCount - 3) is True or willAdaWin \
                (stonesCount - 4) is True:
        return True


for i in range(1, 15):
    print(willAdaWin(i), i)
