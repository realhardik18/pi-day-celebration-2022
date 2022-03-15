import matplotlib.pyplot as plt

with open('pi.txt') as f:
    lines = [line.rstrip() for line in f]
    # reading data from pi.txt
values_lables = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
valeus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for vals in lines:
    vals_ind = list(vals)
    for val in vals_ind:
        valeus[int(val)] += 1

plt.bar(values_lables, valeus, color='blue',
        width=0.5)
plt.xlabel("values")
plt.ylabel("frequency")
plt.title("occurence of digits in pi(upto 1,000,000)")
plt.show()
print(valeus)
# graphing the frecuency
