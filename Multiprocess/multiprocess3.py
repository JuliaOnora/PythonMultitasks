"""
Multiprocess - Módulo concurent.futures em múltiplas tarefas
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
        results = [executor.submit(do_something, 1) for _ in range(10)]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")