import os
import time
import queue
import requests
import datetime
import threading

queue_results = queue.Queue()

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

def loop():
    for i in range(1):
        test_result, elapsed_time = get_request()
        queue_results.put([test_result, elapsed_time])

def test_rps():
    concurrent_user = 8
    workers = []
    start_time = time.time()

    for i in range(concurrent_user):
        thread = threading.Thread(target=loop, daemon=True)
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

    for i in range(qsize):
        try:
            result = queue_results.get_nowait()
        except Empty:
            break
        if result[0] == 200:
            total_pass_requests += 1

    tested_time = end_time - start_time
    rps = total_pass_requests / tested_time
    delay = datetime.timedelta(milliseconds=tested_time * latency)

    assert concurrent_user == total_pass_requests
    assert rps > 5
    assert delay < reference
