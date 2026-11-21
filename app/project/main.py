# def generator1():
#     n = 1
#     while True:
#         n +=1
#         print('inside', n)
#         yield n
#         print('after')
#         yield 5555555555555555
#
# result = generator1()
#
# print(result)
#
# print(next(result))
# print(66666666666666666666666666666)
# print(next(result))
# print(next(result))
# print(next(result))


##########################################################
from time import sleep
import time
#
#
# def hello():
#     print('hello')
#     sleep(2)
#     print('hello again')
#
# def sandwich():
#     print('sandwich')
#     sleep(2)
#     print('sandwich again')
#
# hello()
# sandwich()
##########################################################

import asyncio

async def hello():
    print('hello')
    await asyncio.sleep(2)
    print('hello again')

async def sandwich():
    print('sandwich')
    await asyncio.sleep(2)
    print('sandwich again')


# asyncio.run(hello())
# asyncio.run(sandwich())


async def main():
    await asyncio.gather(
        hello(),
        sandwich(),
        sandwich(),
        sandwich(),
    )

start = time.monotonic()
print(start)

asyncio.run(main())

end = time.monotonic()
print(end)
print(end-start)