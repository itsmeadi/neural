import numpy as n
import matplotlib.pyplot as p
i=n.random.normal(12000,10000,8000)
i.mean()
p.hist(i,50)
p.show()
