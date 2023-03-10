"""
Async - Módulo asyncio em múltiplas tarefas
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import asyncio


async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(3)
    print("Done fetching")
    return {'data': 1}


async def printando_nros():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    # fetch_data() terminará primeiro
    tarefa2 = asyncio.create_task(printando_nros())
    await fetch_data()

    await tarefa2

asyncio.run(main())
