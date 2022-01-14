#!/usr/local/bin/python3
import datetime
import time


def run():
    start = datetime.datetime.now()
    time.sleep(1)
    delta = datetime.datetime.now() - start
    count = 1
    while delta.seconds < 60:

        time.sleep(5)

        now = datetime.datetime.now()
        delta = now - start
        print(f'{now} -- count=[{count}] ')
        count += 1

    print('Job is end. Count should be 12!')


if __name__ == '__main__':
    run()
