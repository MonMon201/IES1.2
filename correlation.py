import numpy as np

def selfcorrelation(x):
  N = len(x)
  Mx = np.mean(x)
  correlation = []
  for tau in range(int(N / 2)):
    r = 0
    for time in range(int(N / 2)):
      r += (x[time] - Mx) * (x[time + tau] - Mx)
    correlation.append(r / (int(N / 2) - 1))
  return correlation

def correlation(x, y):
  N = len(x)
  Mx = np.mean(x)
  My = np.mean(y)
  correlation = []
  for tau in range(int(N / 2)):
    r = 0
    for time in range(int(N / 2)):
      r += (x[time] - Mx) * (y[time + tau] - My)
    correlation.append(r / (int(N / 2) - 1))
  return correlation


def correlation_dict(x, y):
  N = len(x)
  Mx = np.mean(x)
  My = np.mean(y)
  correlation = dict()
  for tau in range(int(N / 2)):
    r = 0
    for time in range(int(N / 2)):
      r += (x[time] - Mx) * (y[time + tau] - My)
    correlation[tau] = (r / ((N / 2) - 1))
  return correlation