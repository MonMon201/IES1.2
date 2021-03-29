import time
import rsg
import correlation as c

def getAvgTime(delta, n, W, d_type = False):
  f = c.correlation if (d_type) else c.correlation_dict
  t = []
  N = []
  for i in range(delta):
    amount = int(10 * (i + 1))
    N.append(amount)
    x = rsg.getRandomSignal(n, W, amount)
    y = rsg.getRandomSignal(n, W, amount)
    start = time.perf_counter()
    f(x, y)
    stop = time.perf_counter()
    t.append(stop - start)
  average = sum(t)/delta
  return N, t, average
