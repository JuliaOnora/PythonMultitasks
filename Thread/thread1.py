"""
Threading - Múltiplas tarefas)
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import time
import threading


def do_something():
    """
    Conta 1 segundo.
    :return: none
    """
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")


threads = []

start = time.perf_counter()

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    print(t)
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")