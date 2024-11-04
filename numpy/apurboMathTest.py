from mpmath import mp
n = int(input("Enter the number of decimal places: "))
mp.dps = n + 1 
print(mp.pi)