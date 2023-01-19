

def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done!')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)


