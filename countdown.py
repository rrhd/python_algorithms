from time import sleep

def countdown(x):
    if isinstance(x, int):
        if x <= 0:
            print('Done!')
        else:
            print(str(x) + '...')
            sleep(1)
            countdown(x - 1)
    else:
        print('Invalid input type.')

countdown(3)