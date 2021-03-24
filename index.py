import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rsg
import correlation as corr

n = 12
W = 2400
N = 1024
time = range(N)
x = rsg.getRandomSignal(n, W, N)
y = rsg.getRandomSignal(n, W, N)

autocorrelation = corr.selfcorrelation(x)
correlation = corr.correlation(x, y)

print(autocorrelation)
print(correlation)

corrR = list(range(N / 2))

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
plt.subplots_adjust(left=0.05, bottom=0.1, right=0.97, wspace=0.1)
fig.suptitle('Lab 1.2')

ax1.plot(x, color='r', label='s 1')
ax1.plot(y, color='g', label = 's 2')
ax1.set_title('Generated signals')
ax1.set(xlabel='time', ylabel='generated signal')
ax1.legend()

ax2.plot(corrR, autocorrelation, color='r')
ax2.set_title('Autocorrelation (s 1)')
ax2.set(xlabel='t', ylabel='correlation')

ax3.plot(corrR, correlation)
ax3.set_title('Cross-correlation')
ax3.set(xlabel='t', ylabel='correlation')

fig.savefig("lab1.png")

plt.show()

