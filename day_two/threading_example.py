import threading
import time
import requests
import random

def fetch_data(url, name):
    print(f"{name} starting...")
    sleep_time = random.uniform(1, 10)  # Simulate variable network delay
    print(f"{name} will take {sleep_time:.2f} seconds to fetch data.")
    time.sleep(sleep_time)  # Simulate variable network delay
    response = requests.get(url)
    print(f"{name} done - Status: {response.status_code}")

# Create threads
threads = []
urls = ["https://api.github.com", "https://api.github.com", "https://api.github.com"]

for i, url in enumerate(urls):
    t = threading.Thread(target=fetch_data, args=(url, f"Thread-{i}"))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads done!")