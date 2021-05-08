import torch
import numpy as np

# 一、创建tensor张量
t=torch.Tensor([1,2,3])
print(t)
# numpy转换为tensor
array=np.arange(12).reshape(3,4)
print('array:',array)
array=torch.Tensor(array)
print('tensor:',array)
# api创建tensor
# 1.创建3行4列的空的tensor，会用无用的数据进行填充
array1=torch.empty([3,4])  # 和torch.empty(3,4)效果一样
print('tensor1',array1)
# 2.创建全为1和0的tensor
array2=torch.ones(3,4)
array3=torch.zeros([3,4])
print('tensor2:',array2,'\n','tensor3:',array3)
# 3.创建随机的tensor，随机值的区间是“rand”[0,1）或"randint"[low,high)或"randn"均值方差满足一定条件的数组
array4=torch.rand([3,4])
print('tensor4:',array4)
array5=torch.randint(low=0,high=10,size=[3,4]) # tensor中用size方法获取形状，而不是np中shape
print('tensor5:',array5)
array6=torch.randn([3,4])  # 随机分布式均值为0，方差为1
print(array6)


# 二、张量的方法和属性
# 1.获取tensor中的数据（当tensor中只有一个元素可用）:tensor.item()
t1=torch.tensor(np.arange(1))
print(t1.item())
t2=torch.Tensor([[[1]]])     # 两个值则获取不到，会报错，如：[[[1,2]]]
print(t2.item())
# 2.转换为numpy数组
t2=t2.numpy()
print(t2)
# 3.获取形状:torch.size()。用size可以获取某一维度的形状时，可以传数据
t3=torch.Tensor([[[1,2]]])
print('t3形状（用shape方法）：',t3.shape)  # 和np中的shape一样
print('t3最后一个维度形状 shape[2] ：',t3.shape[-1])
print('t3形状（用size())方法）：',t3.size())
print('t3最后一个维度形状 size(2) ：',t3.size(-1))  # -1或者写2
# 4.形状修改：tensor.view((3,4))。类似numpy中reshape。是一种浅拷贝，仅仅是形状发生改变
print('t3 view前：',t3)
print('t3 view([2])后变为一阶：',t3.view([2]))
print('t3 view([-1])后变为一阶：',t3.view([-1]))
print('t3 view([2,1])后变为二阶：',t3.view([2,1]))
print('t3 view([2,-1])后变为二阶：',t3.view([2,-1]))
# -1表示后面的形状可以根据前面的形状来确定是什么形状，如果之前是114的形状，那么后面这个就是22的形状
print('也可以用reshape方法改变形状：',t3.reshape([2,1]))
# 5.获取维数（阶数）:torch.dim()
print('t3阶数：',t3.dim())

