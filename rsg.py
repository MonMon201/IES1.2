import random
import math
import time

def getRandomSignal(harmonicsAmount, limitFrequency, N):
    signal = [0] * N
    for i in range (harmonicsAmount):
        w = (limitFrequency / harmonicsAmount) * (i+1)
        A = random.random()
        Fi = random.random()
        for t in range(N):
            signal[t] += (A * math.sin(w * t + Fi))
    return signal