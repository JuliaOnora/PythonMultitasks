"""
Async - Módulo asyncio
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import asyncio


async def main():
    print("Julia")
    await foo("texto")
    print("Terminado")


async def foo(texto):
    print(texto)
    print("Esperando 5 segundos...")
    await asyncio.sleep(5)

asyncio.run(main())
