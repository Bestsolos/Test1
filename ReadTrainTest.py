import pandas as pd
import numpy as np

## 1) 载入训练集和测试集；
path = 'C:/Users/Huang Qiang/Desktop/test/'
Train_data = pd.read_csv(path+'used_car_train_20200313.csv', sep=' ')  ## 训练集录入
Test_data = pd.read_csv(path+'used_car_testA_20200313.csv', sep=' ')   ## 测试集录入

print('Train data shape:',Train_data.shape)
print('TestA data shape:',Test_data.shape)