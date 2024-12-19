import sys
import time
from threading import Thread
from multiprocessing import Process
import math

# 실행 시간 측정
def time_taken(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# 팩토리얼 계산
def compute(num):
    return math.factorial(num)

# 싱글 스레드
@time_taken
def single_thread(nums):
    for num in nums:
        compute(num)

# 멀티 스레드
@time_taken
def multi_thread(nums):
    threads = [Thread(target=compute, args=(num,)) for num in nums]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

# 멀티 프로세싱
@time_taken
def multi_process(nums):
    processes = [Process(target=compute, args=(num,)) for num in nums]
    for process in processes: process.start()
    for process in processes: process.join()

def main():
    nums = [200000] * 6

    single_thread(nums)
    multi_thread(nums)
    multi_process(nums)

if __name__ == "__main__":
    main()
