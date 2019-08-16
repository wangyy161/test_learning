import pandas as pd
import numpy as np
from pandas import DataFrame,Series
data1=pd.DataFrame(np.arange(6).reshape(2,3),columns=list('abc'))
num = 5
data2 = {}
for i in range(num):
    data2[str(i)] = pd.DataFrame(np.arange(20, 26).reshape(2, 3), columns=list('ayz'))
    data1 = pd.concat([data1, data2[str(i)]], axis=1)
print(data1)

# import pandas as pd
# import numpy as np
# from pandas import DataFrame,Series
# data1=pd.DataFrame(np.arange(6).reshape(2,3),columns=list('abc'))
# data2=pd.DataFrame(np.arange(20,26).reshape(2,3),columns=list('ayz'))
