import numpy as np
limit = 10
captains = (lambda n: n[(n % 2 != 0)][:limit])(np.arange(1, limit * 3))
print(captains)
print(np.arange(1, limit * 3)%2)