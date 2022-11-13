"""
任务一1.1（2）：长期数据中客户年龄的预处理
"""

import re
import numpy as np
import pandas as pd

# 读取数据集
data = pd.read_csv("long-customer-train.csv")

# 删除Age取值为0、1、'-'以及缺失值所在的行
data["Age"].replace(['0', '1', '-'], np.nan, inplace=True)
data.dropna(inplace=True)

# 删除Age列中的异常字符，并保留年龄数值
data["Age"] = data["Age"].map(lambda x: re.sub('[岁 ]', '', x))

# 将Age列转化为int整型数据
data["Age"] = data["Age"].astype(int)

# 输出到文件
data.to_excel("result1_2.xlsx", index=False)
