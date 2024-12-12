import multiprocessing
from threading import Thread
import datetime as dt


def read_info(file_name):
    all_data = []
    with open(file_name, 'r') as f:
        while line := f.readline():
            all_data.append(line.strip())


if __name__ == "__main__":
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    now1 = dt.datetime.now()
    for file_name in filenames:
        now = dt.datetime.now()
        read_info(file_name)
        print((dt.datetime.now() - now))
    print(f"Линейное: {dt.datetime.now() - now1}")

    now1 = dt.datetime.now()
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, filenames)
    print(f"Потоковое: {dt.datetime.now() - now1}")