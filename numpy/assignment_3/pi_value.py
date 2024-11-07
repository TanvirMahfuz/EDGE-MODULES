from mpmath import mp
def pi_value(n):
  mp.dps = n + 1 
  return mp.pi