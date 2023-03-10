"""
Python Multitasks - Thread (Módulo Threading)
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import time
import threading

start = time.perf_counter()


def do_something():
    """
    Conta 1 segundo.
    :return: none
    """
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")