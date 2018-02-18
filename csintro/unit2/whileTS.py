
def countdown():
    countdown = 5

    while countdown >= 0:
        print(countdown)
        countdown = countdown - 1

def countdown1():
    countdown = 5
    while countdown >= 0:
        if False:
            break
        print(countdown)
        countdown = countdown - 1


def countdown2():
    countdown = 5
    while countdown >= 0:
        print(countdown)
        countdown = countdown - 1
        break


def countdown3():
    countdown = 5
    while True:
        if countdown >= 0:
            break
        print(countdown)
        countdown = countdown - 1

def countdown4():
    countdown = 5

    while countdown >= 0:
        print(countdown)
        countdown = countdown - 1
        if countdown >=0:
            print(countdown)
            countdown = countdown - 1
        else:
            break



