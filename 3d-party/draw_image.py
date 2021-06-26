import matplotlib.pyplot as plt

filename = '/tmp/perlin4000x4000.binary'
f = open(filename, 'r')

result = []
for i in range(4000):
    tmp = []
    for j in range(4000):
        tmp.append(float(f.readline()[:-1]))
    result.append(tmp)

plt.imshow(result, cmap='gray')
plt.show()
