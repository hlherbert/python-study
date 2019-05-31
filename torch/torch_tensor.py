import torch
import numpy as np

x = torch.Tensor(5,3)
print(x)

y = torch.rand(5,3)
one = torch.ones(5,3)

result = torch.Tensor(5,3)
print(result.size())

view1 = result.view(15)
view2 = result.view(-1,5)
print(view1.size())
print(view2.size())

x = np.arange(6).reshape((2,3))
y = torch.from_numpy(x)
z = y.numpy()

print("np:{}.format:{}".format(x,type(x)))
print("npt-->torch:{}.format:{}".format(y,type(y)))
print("torch-->np:{}.format:{}".format(z,type(z)))

y.add_(1)
print(y)
print(z)