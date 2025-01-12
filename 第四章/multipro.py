from multiprocessing import Process
def func():
    for i in range(1000):
        print('subprocess',i)
if __name__ == "__main__":
    p=Process(target=func)
    p.start()
    for i in range(1000):
        print('main',i)
        