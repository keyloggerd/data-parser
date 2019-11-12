import sys
import matplotlib.pyplot as plt

with open(sys.argv[1]) as f:
    data = f.read()

x = []
y = []
z = []

lines = data.split("\n")
lines = lines[:-1] # data collection gets cut off mid cycle and doesn't matter
                   # at the end anyway
for line in lines:
    parts = line.split()
    x.append(parts[1])
    y.append(parts[2])
    z.append(parts[3])

x = [float(a) for a in x]
y = [float(a) for a in y]
z = [float(a) for a in z]

plt.plot(x)
plt.plot(y)
plt.plot(z)
plt.show()

while True:
    continue
