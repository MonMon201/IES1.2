import numpy as np

def selfcorrelation(x):
  N = len(x)
  Mx = np.mean(x)
  correlation = []
  for tau in range(N / 2):
    r = 0
    for time in range(N / 2):
      r += (x[time] - Mx) * (x[time + tau] - Mx)
    correlation.append(r / ((N / 2) - 1))
  return correlation

def correlation(x, y = []):
  N = len(x)
  Mx = np.mean(x)
  My = np.mean(y)
  correlation = []
  for tau in range(N / 2):
    r = 0
    for time in range(N / 2):
      r += (x[time] - Mx) * (y[time + tau] - My)
    correlation.append(r / ((N / 2) - 1))
  return correlation