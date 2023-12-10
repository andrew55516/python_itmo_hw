import math
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import logging


def integrate_sync(f, a, b, *, n_jobs=1, n_iter=1000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=1000000):
    step = (b - a) / n_iter
    total = 0
    part = n_iter // n_jobs

    def sub_func(start):
        acc = 0
        for i in range(part):
            acc += f(a + (start + i) * step) * step
        return acc

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        results = [executor.submit(sub_func, i * part) for i in range(n_jobs)]
        for future in results:
            total += future.result()

    return total


if __name__ == "__main__":
    logging.basicConfig(filename='task2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    n_jobs_max = multiprocessing.cpu_count() * 2
    test_func = math.cos
    a, b = 0, math.pi / 2

    logging.info("Process with integrate_sync")
    start = time.time()
    res = integrate_sync(test_func, a, b)
    end = time.time()
    logging.info(f"n_jobs: {1}, time: {end - start}, result: {res}")

    for executor_class in [ThreadPoolExecutor, ProcessPoolExecutor]:
        logging.info(f"Process with {executor_class.__name__}")
        for n_jobs in range(1, n_jobs_max+1):
            start = time.time()
            res = integrate(test_func, a, b, n_jobs=n_jobs)
            end = time.time()
            logging.info(f"n_jobs: {n_jobs}, time: {end - start}, result: {res}")
