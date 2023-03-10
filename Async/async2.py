"""
Async - Módulo asyncio
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import asyncio


async def main():
    print("Julia")
    tarefa = asyncio.create_task(foo("texto"))
    await tarefa # retirando essa linha, não será esperada a resolução da linha de nro 11
    print("Terminado")


async def foo(texto):
    print(texto)
    await asyncio.sleep(5)

asyncio.run(main())
