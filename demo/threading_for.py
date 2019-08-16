import threading
import time

def thread1(i):
    print('it is t1 start', i)
    time.sleep(1)
    print('it is t1 finished ', i)

def main():
    for i in range(5):
        t1 = threading.Thread(target=thread1(), args=())
        # 注意thread1后面不能加（），加（）表示的是执行函数（thread1，
        # 没有使用多线程）
        t1.start()
if __name__ == '__main__':
    main()

