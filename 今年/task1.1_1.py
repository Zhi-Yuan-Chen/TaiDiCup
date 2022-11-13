# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 08:21:40 2022

@author: lenovo
"""

import pandas as pd
import numpy as np


short_customer = pd.read_csv('short-customer-data.csv')

id_ser = np.array(range(short_customer.shape[0]))

pre_dulp = short_customer.duplicated(subset=('user_id'))
pre_nan = short_customer.isnull().any(axis=1)

dulps = id_ser[list(pre_dulp)]
nans = id_ser[list(pre_nan)]

short_customer = short_customer.dropna()
short_customer = short_customer.drop_duplicates(subset=('user_id'), keep=False)

short_customer.to_excel('result1_1.xlsx')

