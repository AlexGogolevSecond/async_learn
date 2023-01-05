import multiprocessing
import time
from random import randint
from datetime import datetime
from fib import get_fib


def that_some_thread(n: int) -> None:
    print(f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} привет от процесса: {multiprocessing.current_process()}')
    print(get_fib(n))
    print(f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} выходим из метода в процессе {multiprocessing.current_process()}')


# threads = []
for i in range(6):
    n = randint(40, 41)
    # print(f'поток {i+1} будет спать {sleep} секунд')
    proc = multiprocessing.Process(target=that_some_thread, args=(n,))
    proc.start()
    # threads.append(thr)

# total_process = multiprocessing.pr
# thread_name = threading.current_thread().name
# print(f'в данный момент выполняется {total_threads} потоков')
# print(f'имя текущего потока {thread_name}')

# for i in threads:
#     i.join()

print('the end')





