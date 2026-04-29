import multiprocessing
import time

def cpu_task(n):
    """Compute sum of squares"""
    result = sum(i**2 for i in range(n))
    print(f"Process {multiprocessing.current_process().name}: {result}")
    return result

if __name__ == "__main__":
    # Create processes
    processes = []
    
    for i in range(4):
        p = multiprocessing.Process(target=cpu_task, args=(10000000,))
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    print("All processes done!")