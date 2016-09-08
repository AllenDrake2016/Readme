import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME='thenewboston'
HOMEPAGE='https://thenewboston.com/'
DOMAIN_NAME=get_domain_name(HOMEPAGE) # (thenewboston.com)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAMLED_FILE=PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=8
queue=Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
    # print('main.py/create_workers()')
    for _ in range(NUMBER_OF_THREADS):
        # i=str(i)
        # print('main.py/create_workers()/for loop:'+i)
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()
    # print('main.py/create_workers()/end')
def work():
    print('main.py/work()')
    while True:
        url=queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()
    print('main.py/work()/end')
# Each queued link is a new job
def create_jobs():
    print('main.py/create_jobs()')
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()
    # print('main.py/create_jobs()/end')
# Check if there are items in the queue, if so crawl them
def crawl():
    print('main.py/crawl()')
    queue_links=file_to_set(QUEUE_FILE)
    if len(queue_links)>0:
        print(str(len(queue_links))+'links in the queue')
        create_jobs()
    print('main.py/crawl()/end')

create_workers()
crawl()
