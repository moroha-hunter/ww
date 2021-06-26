import matplotlib.pyplot as plt

filename = '/tmp/perlin4000x4000.binary' #float number on each line, these numbers are Perlin Noise

f = open(filename, 'r')

result = []
for i in range(4000):
    tmp = []
    for j in range(4000):
        tmp.append(float(f.readline()[:-1]))
    result.append(tmp)

plt.imshow(result, cmap='gray')
plt.show()
