## 1.1 图片
    import cv2 as cv
    import sys
### 1.1.1 从文件中读取图像,输出为numpy数组: 
    img = cv.imread("path/*.jpg")
    if img is None:
        sys.exit("Could not read the image.")
### 1.1.2 在OpenCV中显示图像
    cv.imshow("Display window", img)    #创建窗口显示图片
    k = cv.waitKey(0)   #等待键盘输入,0为无限等待
### 1.1.3 将图像写入文件
    cv.imwrite("命名.格式", img)

## 1.2 摄像头捕获实时视频
    import numpy as np
    import cv as cv
### 1.2.1 摄像头初始化
    # 0: 默认摄像头
    # 1: 外接摄像头
    cap = cv.VideoCapture(0)

    #检查摄像头是否开启
    if not cap.isOpened():
        exit()

    # 设置分辨率
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

    # 设置帧率
    cap.set(cv.CAP_PROP_FPS, 30)

### 1.2.2 实时视频循环
    while True:
    # 逐帧捕获
    # ret: 读取是否成功 (True/False)
    # frame: 图像帧 (numpy数组)
    ret, frame = cap.read()
    
    # 检查帧是否读取成功
    if not ret:
        print("❌ 无法接收帧（流结束？）")
        break

### 1.2.3 图像处理操作
    # 图像处理操作示例
    # 转换为灰度图
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # 其他常用处理：
    # blurred = cv.GaussianBlur(frame, (5, 5), 0)        # 高斯模糊
    # edges = cv.Canny(gray, 50, 150)                   # 边缘检测
    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)        # HSV色彩空间

### 1.2.4 显示结果
    # 显示处理后的帧
    cv.imshow('实时视频', gray)
    
    # 按键检测
    # waitKey(1): 等待1毫秒，保持视频流畅
    # ord('q'): 获取'q'键的ASCII码
    if cv.waitKey(1) == ord('q'):
        print("👋 用户退出")
        break

### 1.2.5 资源释放
    # 释放摄像头资源
    cap.release()

    # 关闭所有OpenCV窗口
    cv.destroyAllWindows()

## 1.3 绘制几何形状






