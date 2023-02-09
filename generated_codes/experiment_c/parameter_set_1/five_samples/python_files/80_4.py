
#%%

import pandas as pd
import numpy as np

#%%

i1 = 'I 1.1 2.1 F 70 22'
i2 = 'I 1 4.1 F 37 73'

i3 = 'I 1.1 2.1 F 70 22'
i4 = 'I 1 4.1 F 37 73'
i5 = 'I 1.1 2.1 F 70 22'
i6 = 'I 1 4.1 F 37 73'

i7 = 'I 1.1 2.1 F 70 22'
i8 = 'I 1 4.1 F 37 73'
i9 = 'I 1.1 2.1 F 70 22'
i10 = 'I 1 4.1 F 37 73'

q1 = 'Q 1.1 2 F 10-90'
q2 = 'Q 1 -1 F 30-70'
q3 = 'Q 2 4.1 F 37'


data = pd.DataFrame([i1.split(), i2.split(), i3.split(), i4.split(), i5.split(), i6.split(),
                     i7.split(), i8.split(), i9.split(), i10.split(), q1.split(), q2.split(), q3.split()],
                    columns = ['type', 'product_id', 'province_id', 'sex', 'age', 'units_sold'])

#%%

data['product_id'] = data['product_id'].apply(lambda x: x.split('.')[0])
data['province_id'] = data['province_id'].apply(lambda x: x.split('.')[0])

#%%

data['age'] = data['age'].apply(lambda x: x.split('-')[0])