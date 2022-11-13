"""
任务四：
基于长期数据提取影响客户流失的因素，
构建与银行客户长期忠诚度相关的特征。
"""

import pandas as pd

# 读取数据集
data = pd.read_excel("result3.xlsx", engine='openpyxl')

# 构建新老客户活跃程度的特征
data.loc[(data['Status'] == '新客户') & (data['IsActiveMember'] == 0), 'IsActiveStatus'] = 0
data.loc[(data['Status'] == '稳定客户') & (data['IsActiveMember'] == 0), 'IsActiveStatus'] = 1
data.loc[(data['Status'] == '老客户') & (data['IsActiveMember'] == 0), 'IsActiveStatus'] = 2
data.loc[(data['Status'] == '新客户') & (data['IsActiveMember'] == 1), 'IsActiveStatus'] = 3
data.loc[(data['Status'] == '稳定客户') & (data['IsActiveMember'] == 1), 'IsActiveStatus'] = 4
data.loc[(data['Status'] == '老客户') & (data['IsActiveMember'] == 1), 'IsActiveStatus'] = 5

# 构建不同金融资产客户活跃程度的特征
data.loc[(data['AssetStage'] == '低资产') & (data['IsActiveMember'] == 0), 'IsActiveAssetStage'] = 0
data.loc[(data['AssetStage'] == '中下资产') & (data['IsActiveMember'] == 0), 'IsActiveAssetStage'] = 1
data.loc[(data['AssetStage'] == '中上资产') & (data['IsActiveMember'] == 0), 'IsActiveAssetStage'] = 2
data.loc[(data['AssetStage'] == '高资产') & (data['IsActiveMember'] == 0), 'IsActiveAssetStage'] = 3
data.loc[(data['AssetStage'] == '低资产') & (data['IsActiveMember'] == 1), 'IsActiveAssetStage'] = 6
data.loc[(data['AssetStage'] == '中下资产') & (data['IsActiveMember'] == 1), 'IsActiveAssetStage'] = 7
data.loc[(data['AssetStage'] == '中上资产') & (data['IsActiveMember'] == 1), 'IsActiveAssetStage'] = 8
data.loc[(data['AssetStage'] == '高资产') & (data['IsActiveMember'] == 1), 'IsActiveAssetStage'] = 9

# 构建不同金融资产信用卡持有状态的特征
data.loc[(data['AssetStage'] == '低资产') & (data['HasCrCard'] == 0), 'CrCardAssetStage'] = 0
data.loc[(data['AssetStage'] == '中下资产') & (data['HasCrCard'] == 0), 'CrCardAssetStage'] = 2
data.loc[(data['AssetStage'] == '中上资产') & (data['HasCrCard'] == 0), 'CrCardAssetStage'] = 5
data.loc[(data['AssetStage'] == '高资产') & (data['HasCrCard'] == 0), 'CrCardAssetStage'] = 5
data.loc[(data['AssetStage'] == '低资产') & (data['HasCrCard'] == 1), 'CrCardAssetStage'] = 6
data.loc[(data['AssetStage'] == '中下资产') & (data['HasCrCard'] == 1), 'CrCardAssetStage'] = 7
data.loc[(data['AssetStage'] == '中上资产') & (data['HasCrCard'] == 1), 'CrCardAssetStage'] = 9
data.loc[(data['AssetStage'] == '高资产') & (data['HasCrCard'] == 1), 'CrCardAssetStage'] = 9

# 将特征数值转化为整型变量
data['IsActiveStatus'] = data['IsActiveStatus'].astype(int)
data['IsActiveAssetStage'] = data['IsActiveAssetStage'].astype(int)
data['CrCardAssetStage'] = data['CrCardAssetStage'].astype(int)

# 输出到文件
data.to_excel("result4.xlsx", index=False)
