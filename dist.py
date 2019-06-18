"""距离"""

def l2(x,y):
    """欧氏距离，第二范数"""
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**(0.5)

def l1(x,y):
    """曼哈顿距离，第一范数"""
    return (abs(x[0]-y[0]) + abs(x[1]-y[1]))

def lmax(x,y):
    """上确界距离"""
    dmax = 0
    for i in range(0,len(x)):
        d = abs(x[i] - y[i])
        if d > dmax:
            dmax =d
    return dmax

def length(x):
    """向量长度"""
    return (x[0]**2+x[1]**2)**0.5

def cossim(x,y):
    """余弦相似度"""
    return (x[0]*y[0]+x[1]*y[1])/(length(x)*length(y))

x = [ [1.5,1.7],
      [2.0,1.9],
      [1.6,1.8],
      [1.2,1.5],
      [1.5,1.0]]

y = [1.4,1.6]

print(l2.__doc__)
d2 = []
for xx in x:
    #print(l2(xx,y))
    d2.append(l2(xx,y))
print(d2)

d1=[]
print(l1.__doc__)
for xx in x:
    #print(l1(xx,y))
    d1.append(l1(xx,y))
print(d1)

dmax=[]
print(lmax.__doc__)
for xx in x:
    #print(lmax(xx,y))
    dmax.append(lmax(xx,y))
print(dmax)

dcos=[]
print(cossim.__doc__)
for xx in x:
    dcos.append(cossim(xx,y))
print(dcos)

xplus = x.copy()
print("x",x)
xnorm = xplus.copy()

print("xplus",xplus)
print("y",y)

#0.8   0.9
for i in range(0,len(xplus)):
    xnorm[i][0] = (xnorm[i][0]-1.2)/0.8
    xnorm[i][1] = (xnorm[i][1]-1.0)/0.9
print("xnorm",xnorm)


ynorm = y.copy()
print("ynorm-before",ynorm)
ynorm[0] = (ynorm[0]-1.2)/0.8
ynorm[1] = (ynorm[1]-1.0)/0.9
print("ynorm",ynorm)

print("规范化数据然后求L2")
dnorm = []
for i in range(0,len(xnorm)):
    dnorm.append(l2(xnorm[i],ynorm))
print("dnorm",dnorm)
