## 1.1 基本信息获取
    import pyautogui

    # 获取鼠标当前位置
    current_x, current_y = pyautogui.position()
    print(f"🖱️ 鼠标位置: ({current_x}, {current_y})")

    # 获取屏幕分辨率
    screen_width, screen_height = pyautogui.size()
    print(f"📺 屏幕分辨率: {screen_width}x{screen_height}")

    # 检查坐标是否在屏幕内
    if pyautogui.onScreen(100, 200):
    print("✅ 坐标在屏幕范围内")

## 1.2 安全配置
    # 设置每次操作后的暂停时间（秒）
    pyautogui.PAUSE = 0.5  # 每次操作后暂停0.5秒

    # 启用故障安全模式
    pyautogui.FAILSAFE = True
    # 将鼠标快速移动到左上角(0,0)可立即终止程序

## 1.3 鼠标操作
### 1.3.1 鼠标移动
    # 绝对移动 - 移动到指定坐标
    pyautogui.moveTo(500, 300, duration=1.0)  # 1秒内移动到(500,300)

    # 相对移动 - 相对于当前位置移动
    pyautogui.moveRel(100, -50, duration=0.5)  # 向右100像素，向上50像素

### 1.3.2 鼠标点击
    # 基本点击（左键）
    pyautogui.click()  # 在当前位置点击
    pyautogui.click(x=400, y=300)  # 移动到(400,300)并点击

    # 指定点击参数
    pyautogui.click(
        x=400, y=300,
        clicks=2,           # 点击次数
        interval=0.1,       # 点击间隔（秒）
        button='left'       # 鼠标按钮：'left', 'right', 'middle'
    )

    # 专用点击函数
    pyautogui.rightClick(400, 300)    # 右键点击
    pyautogui.middleClick(400, 300)   # 中键点击  
    pyautogui.doubleClick(400, 300)   # 双击
    pyautogui.tripleClick(400, 300)   # 三击

### 1.3.3 鼠标拖拽
    # 绝对拖拽
    pyautogui.dragTo(600, 400, duration=1.0)  # 拖拽到指定位置

    # 相对拖拽  
    pyautogui.dragRel(200, 100, duration=1.0)  # 相对当前位置拖拽

### 1.3.4 鼠标滚动
    # 滚动鼠标滚轮
    pyautogui.scroll(10)    # 向上滚动10个单位
    pyautogui.scroll(-10)   # 向下滚动10个单位
    pyautogui.scroll(5, x=400, y=300)  # 在指定位置滚动

### 1.3.5 分离按下和释放
    # 分别控制按下和释放
    pyautogui.mouseDown(x=400, y=300, button='left')   # 按下鼠标
    # ... 执行其他操作 ...
    pyautogui.mouseUp(x=400, y=300, button='left')     # 释放鼠标

## 1.4 键盘操作
### 1.4.1 文本输入
    # 输入文本
    pyautogui.typewrite('Hello World!\n', interval=0.1)  # 输入文本，每个字符间隔0.1秒

    # 输入特殊键序列
    pyautogui.typewrite(['a', 'b', 'left', 'backspace', 'enter', 'f1'], interval=0.05)
    
### 1.4.2 快捷键操作
    # 组合快捷键
    pyautogui.hotkey('ctrl', 'c')      # Ctrl+C 复制
    pyautogui.hotkey('ctrl', 'v')      # Ctrl+V 粘贴
    pyautogui.hotkey('ctrl', 'shift', 'esc')  # 三键组合

    # 分离按键操作
    pyautogui.keyDown('ctrl')    # 按下Ctrl
    pyautogui.press('c')         # 按下并释放C
    pyautogui.keyUp('ctrl')      # 释放Ctrl
    
### 1.4.3 可用键名列表
    # 常用特殊键：
    'enter', 'tab', 'space', 'backspace', 'esc',
    'f1' 到 'f12', 
    'left', 'right', 'up', 'down',
    'home', 'end', 'pageup', 'pagedown',
    'ctrl', 'alt', 'shift', 'win'

    # 查看所有可用键
    print(pyautogui.KEYBOARD_KEYS)

## 1.5 消息框功能
### 1.5.1 用户交互对话框
    #警告对话框（只有确定按钮）
    pyautogui.alert('程序即将开始自动化操作！', '警告')

    # 确认对话框（确定和取消）
    result = pyautogui.confirm('是否继续执行？', '确认')
    if result == 'OK':
    print("用户选择了继续")
    else:
        print("用户取消了操作")

    # 输入对话框
    user_input = pyautogui.prompt('请输入您的姓名：', '输入')
    print(f"用户输入: {user_input}") 

## 1.6 截图与图像识别
### 1.6.1 屏幕截图
    # 截图并保存
    screenshot = pyautogui.screenshot('screenshot.png')  # 保存为文件
    print(f"截图尺寸: {screenshot.size}")  # 输出: (1920, 1080)

    # 只获取截图对象
    screenshot = pyautogui.screenshot()

### 1.6.2 图像识别定位
    # 在屏幕上查找图像
    button_location = pyautogui.locateOnScreen('button.png')
    if button_location:
        print(f"找到按钮位置: {button_location}")  # (x, y, width, height)

    # 查找所有匹配位置
    all_locations = list(pyautogui.locateAllOnScreen('icon.png'))
    for loc in all_locations:
        print(f"找到图标: {loc}")
    
    # 直接获取中心坐标
    center = pyautogui.locateCenterOnScreen('target.png')
    if center:
        x, y = center
        pyautogui.click(x, y)  # 点击找到的图像中心
