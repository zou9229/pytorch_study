import time
import random
from pymouse import PyMouse
m = PyMouse()


while (1):
    m.click(430, 570)  # 移动并且在(x,y)位置左击
    time.sleep(1.5)
    m.click(random.randint(850,855), random.randint(258,263))  # 移动并且在(x,y)位置左击
    time.sleep(9)
    #
    # m.click(760,320 )  # 移动并且在(x,y)位置左击
    # time.sleep(6)



# import os
# # 图片二值化
# from PIL import Image
# import numpy as np
# import cv2
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #定义一个核
# path = 'C:\/Users\/92381\/Desktop\/210608-HZ-YH-011\/CROP-XKW-HZ-210608-7-030'
# path_list = os.listdir(path)
# print(path_list)
#
# img = Image.open('t.jpg')
#
# # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# Img = img.convert('L')
# Img.save("test1.jpg")
#
# # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
# threshold = 150
#
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# # 图片二值化
# photo = Img.point(table, '1')
# photo.save("test2.jpg")
#
# photo=cv2.imread("test2.jpg")
# photo = cv2.filter2D(photo, -1, kernel=kernel)
# cv2.imwrite('save.jpg',photo)
#
#
#
#
#
#
#
# import sys
# import threading
# import pythoncom
# import pyWinhook
# thread_list = []
#
# def click():
#     time.sleep(1)
#     print('click!!!')

# def onKeyboardEvent(event):
#     print('keboard!!!event!!!')
#     # 监听键盘事件
#     if(event.KeyID==32):
#         sys.exit()
#     # 同鼠标事件监听函数的返回值
#     return True
# def keyboard():
#     time.sleep(1)
#     print('kryboard!!!')
#     # 创建一个“钩子”管理对象
#     hm = pyWinhook.HookManager()
#
#     # 监听所有键盘事件
#     hm.KeyDown = onKeyboardEvent
#     # 设置键盘“钩子”
#     hm.HookKeyboard()
#
#     # 进入循环，如不手动关闭，程序将一直处于监听状态
#     pythoncom.PumpMessages()
#
#
# th1 = threading.Thread(target=click) ##创建线程
# th2 = threading.Thread(target=keyboard)
# thread_list.append(th1)
# thread_list.append(th2)
# for th in thread_list:
#     th.start()
# for th in thread_list:
#     th.join()