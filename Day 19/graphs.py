import matplotlib.pyplot as plt

xpoints = [1,2,3,4,10]
ypoints = [2,4,6,8,10]

# plt.plot(xpoints, ypoints)
# plt.show()


sizes = [20,50,20,30]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels)
plt.axis('equal')

plt.show()
