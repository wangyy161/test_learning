import time, threading

event = threading.Event()

# 交通灯
def lighter():
    count = 0
    while True:
        if count < 5:  # 绿灯
            event.set()  #设置标志位
            print("\033[42;1m 绿灯亮\033[0m")
        elif count > 10:
            count =0  # 清零重新计数
        else:  # 红灯
            event.clear()  # 清空标志位
            print("\033[41;1m 红灯亮\033[0m")

        time.sleep(1)
        count += 1

# 车辆
def car(name):
    while True:
        if event.is_set():  # 绿灯亮
            print("[%s]绿灯行..." % name)
            time.sleep(1)
        else:
            print("[%s]红灯停!!!" % name)
            event.wait()  # 等待标志位设定
            print("\033[34;1m绿灯出发\033[0m")

# 启动交通灯
t_lighter = threading.Thread(target=lighter) # 添加线程，target表示的是执行的功能
t_lighter.start()

# 放入车辆
t_car1 = threading.Thread(target=car, args=("奥迪车",))
t_car2 = threading.Thread(target=car, args=("大众车",))
t_car1.start()
t_car2.start()
