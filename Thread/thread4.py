"""
Python Multitasks - Thread (Módulo Concurrent)
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""


import time
import concurrent.futures


def do_something(seconds):
    """
    Conta segundos.
    :param seconds: int
    :return: none
    """
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done Sleeping..."


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f = executor.submit(do_something, 2)
    print(f.result())

threads = []


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")