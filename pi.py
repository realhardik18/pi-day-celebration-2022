import decimal
import matplotlib.pyplot as plt

negative = False
curr = 1
pi = 0
for i in range(100000):
    if i % 2 == 0:
        pi += 4/curr
        curr += 2
    else:
        pi -= 4/curr
        curr += 2

d2 = decimal.Decimal(pi)
dot100 = decimal.Context(prec=1000000)
d2 *= d2
pi = d2.sqrt(dot100)
print(type(pi))
# copied this output to pi.txt(after the decimal place)
