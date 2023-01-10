import time


try:
    while True:
        time.sleep(1)
        print('lalala')
except KeyboardInterrupt as ex:
    print('поймали исключение KeyboardInterrupt: {ex}'.format(ex=ex))

