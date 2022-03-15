import decimal
import matplotlib.pyplot as plt

curr = 1
pi = 0
for i in range(100000):
    if i % 2 == 0:
        pi += 4/curr
        curr += 2
    else:
        pi -= 4/curr
        curr += 2

pi_acc = decimal.Decimal(pi)
dot100 = decimal.Context(prec=1000000)
pi_acc *= pi_acc
pi = pi_acc.sqrt(dot100)
print(type(pi))
# copied this output to pi.txt(after the decimal place)
