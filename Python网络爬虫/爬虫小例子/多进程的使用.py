from multiprocessing import Process,Pool
import time
import os
# import calendar

def run(name):
	print("{0} is running".format(name))
	time.sleep(3)
	print("{0} is ending".format(name))


if __name__ == '__main__':
	p = Pool(10)
	for i in range(10):
		print("{0} is running".format(i))
		p.apply_async(run,args=(i,))
	p.close()
	p.join()
	print("hhh")




# -*- coding:utf-8 -*-


# from multiprocessing import Process,Pool
# import os,time

# def run_proc(name):        ##定义一个函数用于进程调用
#     for i in range(5):    
#         time.sleep(0.2)    #休眠0.2秒
#         print("{0} is running".format(name))
# #执行一次该函数共需1秒的时间

# if __name__ =='__main__': #执行主进程
#     mainStart = time.time() #记录主进程开始的时间
#     p = Pool(8)           #开辟进程池
#     for i in range(16):                                 #开辟14个进程
#         p.apply_async(run_proc,args=('Process'+str(i),))#每个进程都调用run_proc函数，
#                                                         #args表示给该函数传递的参数。
#     p.close() #关闭进程池
#     p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行
#     mainEnd = time.time()  #记录主进程结束时间
