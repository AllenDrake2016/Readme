from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
class Spider:
    # Class variable (shared among all instances)
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    append_file=''
    queue=set()
    crawled=set()
    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name=project_name
        Spider.base_url=base_url
        Spider.domain_name=domain_name
        Spider.queue_file=Spider.project_name+'/queue.txt'
        Spider.crawled_file=Spider.project_name + '/crawled.txt'
        Spider.append_file=Spider.project_name+'/append.txt'
        self.boot()
        self.crawl_page('First spider',Spider.base_url)
        # print('end')

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)
        Spider.queue=file_to_set(Spider.queue_file)
        Spider.crawled=file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url): #https://thenewboston.com/
        if page_url not in Spider.crawled:
            print(thread_name+'now crawling'+page_url)
            print('Queue'+str(len(Spider.queue))+'| Crawled'+str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url),page_url)
            if len(Spider.queue)==0:
                Spider.queue = file_to_set(Spider.queue_file)
            else:
                Spider.queue.remove(page_url)
                Spider.crawled.add(page_url)
                Spider.update_files()


    @staticmethod
    def gather_links(page_url):
        html_string=''
        try:
            response=urlopen(page_url)
            if response.getheader('Content-Type')=='text/html':
                html_bytes=response.read()
                html_string=html_bytes.decode("utf-8")
            finder=LinkFinder(Spider.base_url,page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            return set()
        # print(finder.page_links())
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links,currentLink):
        for url in links:
            append_to_file(Spider.queue_file, url)
            if url not in Spider.queue:
                continue
            if url not in Spider.crawled:
                continue
            if Spider.domain_name in url:
                continue
            links.remove(url)
        set_to_file(links, Spider.queue_file)
            # set_to_file(links,Spider.queue_file)
        set_to_append_file(links,Spider.append_file,currentLink)
    @staticmethod
    def update_files():
        ## set_to_file(Spider.queue,Spider.queue_file)
        # print('update_file/Spider.queue | Spider.queue_file look here!'+str(Spider.queue),'|',Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)
