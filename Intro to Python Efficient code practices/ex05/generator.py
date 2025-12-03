import sys
import time
import resource


def read_file_generator(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def get_memory_usage():
    if hasattr(resource, 'getrusage'):
        memory_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return memory_kb / (1024 * 1024)
    else:
        import os
        import psutil
        print('Windows')

        process = psutil.Process(os.getpid())
        memory_mb = process.memory_info().rss / (1024 * 1024)
        return memory_mb / 1024



def main():
    if len(sys.argv) != 2:
        print("Usage: python generator.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()
    lines_generator = read_file_generator(filename)

    for line in lines_generator:
        pass

    end_time = time.time()
    peak_memory = get_memory_usage()
    total_time = end_time - start_time

    print(f"Peak Memory Usage = {peak_memory:.3f} GB")
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s")


if __name__ == "__main__":
    main()