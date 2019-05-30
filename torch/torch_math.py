import numpy
import torch


data=[-1,-2,1,2]
tensor = torch.FloatTensor(data)
print(
    '\nabc',
    '\nnumpy:',numpy.abs(data),
    '\ntorch:',torch.abs(tensor)
)

# matrix multiplication
data = [[1,2],
        [3,4]]

#1,2          1,2
#3,4          3,4
tensor = torch.FloatTensor(data)
print(
    '\nmatrix multiplication (matmul)',
    '\nnumpy:',numpy.matmul(data,data),
    '\ntorch:',torch.mm(tensor,tensor)
)

# 下面是错误的方法
data = numpy.array(data)
print('data:',data)
print(
    '\nmatrix multiplication (dot)',
    '\nnumpy:',data.dot(data),
    '\ntorch:',tensor.dot(tensor)
)