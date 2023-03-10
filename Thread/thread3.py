"""
Python Multitasks - Thread (Módulo Threading em múltiplas tarefas, caso 2)
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import time
import threading

start = time.perf_counter()


def do_something(seconds):
    """
    Conta segundos.
    :param seconds: int
    :return: none
    """
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done Sleeping...")


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")