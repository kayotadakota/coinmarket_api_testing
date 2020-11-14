import os
import math
import time
import queue
import requests
import datetime
import threading

queue_results = queue.Queue()

def percentile(lst, percent):
    if not lst:
        return None
    index = math.floor(len(lst) * percent)
    return lst[int(index)]

def get_request():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'
    params = {
        'limit': 10,
        'sort': 'volume_24h'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.environ['coinmarket']
    }
    response = requests.get(url, headers=headers, params=params)

    return response.status_code, response.elapsed.total_seconds()

def test_rps():
    concurrent_user = 8
    workers = []
    start_time = time.time()

    for i in range(concurrent_user):
        test_result, elapsed_time = get_request()
        thread = threading.Thread(args=(test_result, elapsed_time), daemon=True)
        queue_results.put([test_result, elapsed_time])
        thread.start()
        workers.append(thread)

    for w in workers:
        w.join()

    end_time = time.time()

    rps = 0
    reference = datetime.timedelta(milliseconds=450)
    total_pass_requests = 0
    qsize = queue_results.qsize()
    latency = 0.8 # 80%
    data = []

    for i in range(qsize):
        try:
            result = queue_results.get_nowait()
            data.append(round(result[1], 3))
        except Empty:
            break
        if result[0] == 200:
            total_pass_requests += 1

    tested_time = end_time - start_time
    rps = total_pass_requests / tested_time

    assert concurrent_user == total_pass_requests
    assert rps > 5
    assert percentile(sorted(data), latency) < 450
