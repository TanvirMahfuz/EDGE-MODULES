import numpy as np
from mpmath import mp
import pandas as pd
import csv
def pi_digits(n):
    mp.dps = n + 1  # Set decimal places
    return str(mp.pi)  # Return pi as a string

with open('pi_digits.txt', 'w') as f:
    f.write(pi_digits(1000000)[2:])
