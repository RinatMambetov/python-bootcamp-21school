import sys
import time
import httpx

if len(sys.argv) < 2:
    print('Usage: python crawl.py url1 [url2 ...]')
    sys.exit(1)

urls = sys.argv[1:]

task_endpoint = 'http://localhost:8888/api/v1/tasks/'
status_endpoint = 'http://localhost:8888/api/v1/tasks/{}'
tasks = {}

data = {'data': [{'url': url} for url in urls]}

with httpx.Client() as client:
    response = client.post(task_endpoint, json=data)
    response.raise_for_status()
    task_id = response.json()['task_id']
    tasks[task_id] = urls

while any(status != 'ready' for status in tasks.values()):
    for task_id, urls in tasks.items():
        if tasks[task_id] == 'ready':
            continue

        with httpx.Client() as client:
            response = client.get(status_endpoint.format(task_id))
            response.raise_for_status()

        if response.json()['status'] == 'ready':
            tasks[task_id] = 'ready'
            response_codes = response.json()['result']

            for i, response_code in enumerate(response_codes):
                print(f'{response_code}\t{urls[i]}')
