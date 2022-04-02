import numpy as np
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(x[1][2])
#
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(x.ndim)   # 2
# print(x.size)   # 9
# print(x.shape)  # (3, 3)

# x = np.array([2, 7, 3])
# x = np.append(x, 4)
# print(x)
# x = np.delete(x, 0)
# print(x)
# x = np.sort(x)
# print(x)
# x = np.size(x)                            !!!!!!   size = len !!!!!!!
# print(x)
# z = np.arange(2, 55, 6)
# print(z)

# x = np.arange(1, 8, 3)
# print(x)
# z = x.reshape(3, 1)
# print(z)
# print(z[1][0])

# x = np.arange(1, 10)
# print(x)
# print(x[0:2])
# print(x[5:])
# print(x[:2])
# print(x[-3:]

# x = np.arange(1, 10)
# print(x[x < 4])
# print(x[(x > 5) & (x % 2 == 0)])
# print(x.sum())
# r = x * 2
# print(r)
# z = [i * 2 for i in x if i % 2 == 0]
# print(z)

x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])
print(np.mean(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))
