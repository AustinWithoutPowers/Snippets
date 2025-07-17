import time

def get_cpu_time():
    start = time.process_time()
    # Do stuff
    end = time.process_time()
    print(f'CPU time taken: {end - start}s')

def get_elapsed_time():
    start = time.time()
    # Do stuff
    end = time.time()
    print(f'Elapsed time taken: {end - start}s')

def get_times():
    cpu_start = time.process_time()
    current_start = time.time()
    # Do stuff
    cpu_end = time.process_time()
    current_end = time.time()
    print(f'CPU time taken: {cpu_end - cpu_start}s')
    print(f'Elapsed time taken: {current_end - current_start}s')