import os

# Each website crawl is a seperate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project'+directory)
        os.makedirs(directory)


def create_data_files(project_name,base_url):
    queue=project_name +'/queue.txt'
    crawl=project_name+'/crawled.txt'
    append=project_name+'/append.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawl):
        write_file(crawl,'')
    if not os.path.isfile(append):
        write_file(append,base_url)
# Create a new file
def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()

#create_data_files('thenewboston','https://thenewboston.com/')

# Add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

# Delete the contents of a file
def delete_file_contents(path):
    with open(path,'w'):
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    # print("general/file_to_set/result look here!"+str(results))
    return results


def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)

def set_to_append_file(links,file,currentLink):
    header='####################################################### '+currentLink
    append_to_file(file,header)
    for link in sorted(links):
        append_to_file(file,link)


