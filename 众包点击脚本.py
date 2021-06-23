import time
import random
from pymouse import PyMouse
m = PyMouse()
while (1):
    m.click(310, 550)  # 移动并且在(x,y)位置左击
    time.sleep(2.5)
    m.click(790, 260)  # 移动并且在(x,y)位置左击
    time.sleep(random.randint(9,12))

# while (1):
#     m.click(760,320 )  # 移动并且在(x,y)位置左击
#     time.sleep(6)












import sys
import threading
import pythoncom
import pyWinhook
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