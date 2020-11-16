# -*- coding: utf-8 -*-
# @Time : 2020/11/16 17:49
# @Author : wianwu
# @Software: PyCharm 
'''
IP camera by opencv4
'''

import cv2
import time


def IpCamera_pyOpencv():
    '''
    通过 poencv-python 获取IP camera 视频流动：
    体现了opencv 拉流的强大！！！！！
    :return:
    '''

    ID = 0
    # IP = 'http://172.29.131.135:8888/stream/live.jpg?id=' + str(i)
    IP = 'http://172.29.111.221:8888/stream/live.jpg?id=' + str(
        ID)  # Xianwu: 通过IP camera app提供的连接，先在浏览中打开，然后查找元素点击画面，找到视频流地址复制下

    try:
        while (1):
            cap = cv2.VideoCapture(IP)
            _, frame = cap.read()
            cv2.imshow("aa", frame)
            if cv2.waitKey(1) == ord('q'):  # 退出 ;不知道是不是这里检测按键时间过长，但是没有这个好像又不行
                break
            ID += 1

    except Exception as e:
        print(e)

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 释放窗口
