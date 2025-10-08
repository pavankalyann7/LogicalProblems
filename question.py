# #multithreading vs threading
# #threading : python by default Python runs single-threaded duo to GIL(GLOBEL INTERPRETER LOCK) PYTHON ONE THREAD EXECUTES bytecode at a time.
# import time
# import threading
# def from10to1000():
#     a = time.time()
#     c = 0
#     for i in range(10,100000):
#         c+=1
#     print(c)
#     b = time.time()
#     print(b - a)

# #multithreading
# def from10to10000():
#     a = time.time()
#     c = 0
#     for i in range(10,1000000):
#         c+=i
#     print(c)
#     b = time.time()
#     print(b -a)
# second = threading.Thread(target=from10to10000,args=())
# first=threading.Thread(target=from10to1000,args=())

# first.start()
# second.start()

# first.join()
# second.join()
# '''
# 🔹 Explanation:
# threading.Thread → creates a new thread for each function.
# start() → begins execution of that thread.
# join() → tells the main program to wait until that thread finishes.
# Now addition and subtraction run “at the same time” (parallel execution is simulated, but because of the GIL, only one runs at a time — still useful for I/O tasks).
# '''
# import threading
# import time

# def task(name):
#     print(f"{name} starting...")
#     time.sleep(2)
#     print(f"{name} finished.")

# t1 = threading.Thread(target=task, args=("Thread-1",))
# t2 = threading.Thread(target=task, args=("Thread-2",))

# t1.start()
# t2.start()
# t1.join()
# t2.join()
import multiprocessing
import time

def task(name):
    
    print(f"{name} starting...")
    time.sleep(2)
    print(f"{name} finished.")

if __name__ == "__main__":   # ✅ Required on Windows
    p1 = multiprocessing.Process(target=task, args=("Process-1",))
    p2 = multiprocessing.Process(target=task, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

