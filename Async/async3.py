"""
Async - Módulo asyncio em múltiplas tarefas
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import asyncio


async def fetch_data():
    print("Start fetching... Wait 3 seconds")
    await asyncio.sleep(3)
    print("Done fetching")
    return {'data': 1}


async def printando_nros():
    print("Will print each 5 seconds")
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    tarefa1 = asyncio.create_task(fetch_data())
    tarefa2 = asyncio.create_task(printando_nros())

    valor = await tarefa1
    print(valor)

    await tarefa2 # sem esta linha, não se espera terminar "tarefa2"

asyncio.run(main())
