import matplotlib.pyplot as plt
from data import correlation, api

fig, ax = plt.subplots()
x = api.trend_request(['Python'])[:, 0]
y = api.trend_request(['Java'])[:, 0]
ax.scatter(x, y)
cov = correlation.covariance(list(x), list(y))
print(cov)
plt.show()
