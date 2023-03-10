"""
Multiprocess - Múltiplas tarefas (Módulo multiprocessing)
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import time
import multiprocessing


def do_something(seconds):
    """
    Contagem de segundos.
    :param seconds: int
    :return: none
    """
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done Sleeping...")


if __name__ == '__main__':

    start = time.perf_counter()

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")