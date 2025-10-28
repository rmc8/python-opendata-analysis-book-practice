import time


def time_magic(fx):
    def inner(*args, **kwargs):
        print(f"--- {fx.__name__} を実行します ---")
        start_time = time.time()
        result = fx(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"--- 実行時間： {elapsed_time:.4f}秒 ---")
        return result

    return inner
