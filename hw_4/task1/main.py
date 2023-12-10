import time
import threading
import multiprocessing


def fib(n):
    f1, f2 = 1, 1
    while n > 2:
        f1, f2 = f2, f1 + f2
        n -= 1
    return f2


def measure_time(method, n, count=10):
    start = time.time()
    threads_processes = []
    for _ in range(count):
        t_p = method(target=fib, args=(n,))
        t_p.start()
        threads_processes.append(t_p)
    for t_p in threads_processes:
        t_p.join()
    return time.time() - start


if __name__ == "__main__":
    n = 1000000

    start = time.time()
    for _ in range(10):
        fib(n)
    sync = time.time() - start

    thread = measure_time(threading.Thread, n)

    process = measure_time(multiprocessing.Process, n)

    with open("timing.txt", "w") as file:
        file.write(f"Синхронное выполнение: {sync} секунд\n")
        file.write(f"Многопоточность: {thread} секунд\n")
        file.write(f"Многопроцессорность: {process} секунд\n")
