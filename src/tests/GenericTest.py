import schedule


'''
Simple Scheduler example
'''
def scheduler():
    ret1 = schedule.every(2).seconds.do(myJob) 
    print("ret1:", ret1)
    while True:
        ret2=schedule.run_pending()
        print(schedule.get_jobs())


def myJob():
    return "called"

#scheduler()



'''
Simple multiprocessing example
'''
from multiprocessing import Process, Manager
import time

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        print(d)
        print(l)
        time.sleep(5)
        p.join()

        print(d)
        print(l)
