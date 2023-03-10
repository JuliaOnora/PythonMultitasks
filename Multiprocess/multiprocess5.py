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
    return f"Done Sleeping...{seconds}"


if __name__ == '__main__':

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")