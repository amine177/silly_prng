#!/bin/env python


import datetime
import math


def random():

    date = datetime.datetime.now()
    seed = []
    seed.append(date.day)
    seed.append(date.month)
    seed.append(date.second)
    seed.append(date.microsecond)
    seed.append(date.minute)
    seed.append(date.hour)

    sum = 0.0
    for i in seed:
        sum += i
    sum += 0.1
    product = date.microsecond * (sum / (date.microsecond + 0.01))
    for i in seed:
        product *= i
    product += 0.1

    x = math.tanh(((product / sum + sum / product) / product))
    y = int(str(x)[8:11])
    x = y * x
    while x > 1:
        x = x / 10
    while x < 0.1:
        x = x * 10

    y = str(x)[2:]
    s = 1
    for i in y:
        s += (int(int(i)*s) << 2)

    x = s >> int((datetime.datetime.now().minute / 30))

    while x > 1:
        x = x / 10
    while x < 0.1:
        x = x * 10

    return x


if __name__ == "__main__":
    for i in range(100):
        print(int(random() * 100))
