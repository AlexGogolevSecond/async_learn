import threading
import time
from random import randint
from datetime import datetime


def that_some_thread(n: int) -> None:
    print(f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} привет от потока: {threading.current_thread()}')
    time.sleep(n)
    print(f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} выходим из метода в потоке {threading.current_thread()}')


threads = []
for i in range(6):
    sleep = randint(1, 5)
    print(f'поток {i+1} будет спать {sleep} секунд')
    thr = threading.Thread(target=that_some_thread, args=(sleep,))
    thr.start()
    threads.append(thr)

total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f'в данный момент выполняется {total_threads} потоков')
print(f'имя текущего потока {thread_name}')

# for i in threads:
#     i.join()

print('the end')





