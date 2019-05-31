import torch
from torch.autograd import Variable

xx = torch.ones(3)
var = Variable(xx, requires_grad=True)

yy = var*2
zz = yy*yy
print('var=',var)
print('zz=',zz)

gradi = torch.Tensor([1,0.1,0.003])
zz.backward(gradi)
print(var.grad)