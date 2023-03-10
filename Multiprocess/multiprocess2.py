"""
Multiprocess - Módulo concurent.futures
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""
import time
import concurrent.futures


def do_something(seconds):
    """
    Contagem de segundos.
    :param seconds: int
    :return: none
    """
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return "Done Sleeping..."


if __name__ == '__main__':

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")