# 分类
import torch
import matplotlib.pyplot as plt

# data
n_data = torch.ones(100,1)

x0 = torch.normal(2*n_data, 1)
y0 = torch.normal(2*n_data, 1)

x1 = torch.normal(-2*n_data, 1)
y1 = torch.normal(-2*n_data, 1)

x = torch.cat((x0,x1),0).type(torch.FloatTensor)
y = torch.cat((y0,y1),).type(torch.LongTensor)

plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()