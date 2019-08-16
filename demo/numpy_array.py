import numpy
import numpy as np
b = numpy.zeros((2,81))
a = list(numpy.random.randint(10, size=10))
c = list(numpy.random.randint(10, size=10))
d = np.vstack((a,c))
b[:,0:10] = d
cc = list(b.flatten('F'))
a.extend(cc)
for asd in b:
    a.extend(asd)
print(a)




