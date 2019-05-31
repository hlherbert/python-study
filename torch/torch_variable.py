import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor, requires_grad=True)

print(tensor)
print(variable)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)
print(t_out)
print(v_out)

v_out.backward()
print(variable.grad)

print(variable)
print(variable.data)
print(variable.data.numpy())

x=Variable(torch.ones(2,2), requires_grad=True)
#x=Variable(torch.ones(2,2))
print(x)
vairable_np = x.data.numpy()

y = x+2
z = y*y*3
print(y)
print(y.grad_fn)
print(z.grad_fn)
print('z=',z)

out = z.mean()
print('out=',out)
out.backward()
print(x.grad)