import torch
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 一、前向计算，对于pytorch的一个tensor，如果设置它的属性.requires_grad为Ture，
#   那么它将会追踪对于张量的所有操作。或者说，这个tensor是一个参数，后续会被计算题都，更新该参数。
# 1.计算过程
x=torch.ones(2,2,requires_grad=True,device=device)  # 初始化参数x并设置
# requires_grad=True用来追踪其计算历史
print(x)
y=x+2
print(y)
z=y*y*3
print(z)
out=z.mean()
print(out)
# x的requires_grad属性为True，之后的每次计算都会修复其grad_fn属性，用来记录做过的操作
# 通过这个函数和grad_fn能够组成一个和前一小节类似的计算图
a=torch.randn(2,2)
a=((a*3)/(a-1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b=(a*a).sum()
print(b.grad_fn)
with torch.no_grad():  # 如果我们有一次不想记录梯度(为了防止跟踪历史记录和使用内存）
    c=(a*a).sum()  # 此时c没有grad_fn，在评估模型时特别有用，因为模型可能具有require_grad=Ture的可训练的参数，但是我们不需要在此过程对他们进行梯度计算。
    print(c)
print(c.requires_grad)
# 2.梯度计算
# 对于1中的out而言，我们可以使用backward方法来进行反向传播，
# 计算梯度out.backward()，此时便能够求出导数dout/dx,使用x.grad能够获取导数值
out.backward()
print(x.grad)  # x.grad会累加梯度，所以每次获取新的梯度需要先把backward置为0
# 当requir_grad=Ture时，tensor.data仅仅是获取tensor中的数据
b=a
b.requires_grad_(True)
print(b)
print(b.data)
# requires_grad=True不能直接转换numpy，需要使用tensor.detach().numpy
# data浅拷贝，改b值b.data也改，detach深拷贝，不会改