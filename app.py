from test import Car
from threading import Thread
run = Car()

def runall():
    if __name__ == '__main__':
        Thread(target=run.AcceptCookies).start()
        Thread(target=run.CarSearching).start()


runall()