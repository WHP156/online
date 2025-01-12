from threading import Thread
def func(name):
    for i in range(1000):
        print(name,i)


if __name__=='__main__':
    t=Thread(target=func,args=('jj',))
    t.start()#加状态
    for i in range(1000):
        print('main',i)
#the second method
# class Mythread(Thread):
#     def run(self):
#         for i in range(1000):
#             print('sublining',i)

# if __name__ == "__main__":
#     t=Mythread()
#     t.start()
#     for i in range(1000):
#         print('main',i)