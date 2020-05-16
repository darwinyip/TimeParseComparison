from datetime import datetime
from time import time


if __name__ == '__main__':
    time_str = "2019-12-24 05:30:29 UTC"
    time_format = "%Y-%m-%d %H:%M:%S %Z"
    time_epoch = 1577183429
    it = 1000000

    print("start...")

    start = time()
    for _ in range(it):
        datetime.strptime(time_str, time_format)
    print("Parse string: ", (time() - start) / it)  # 10^-5

    start = time()
    for _ in range(it):
        datetime.fromtimestamp(time_epoch)
    print("Parse epoch:", (time() - start) / it)  # 10^-7
