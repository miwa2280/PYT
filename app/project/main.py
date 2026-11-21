from time import sleep
import sys

# print(sys.argv)

n = 0
limit = int(sys.argv[1])

while True:
    n += 1
    print(n)
    sleep(1)
    if n >= limit:
        break