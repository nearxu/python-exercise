import numpy as np

a =np.array([[30,40,70],[80,20,10],[50,90,60]])


# 百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比
print(np.percentile(a,40))
print(np.median(a))

print(np.percentile(a,40,axis=1))