#a simple python web crawler 

import urllib
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""



def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


def add_to_index(index, keyword, url):
    if keyword in index:
        #print index[keyword]
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def compute_ranks(graph):
    d = 0.8 #damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for link in graph:
                if page in graph[link]:
                    newrank += d * ranks[link] / len(graph[link])
            newranks[page] = newrank
        ranks = newranks
    return ranks


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def lucky_search(index, ranks, keyword):
    if keyword not in index:
        return None
    else:
        links = index[keyword]
        return_link = ''
        max = 0
        for link in links:
            if ranks[link] > max:
                max = ranks[link]
                return_link = link
        return return_link

#Here is an example showing a sequence of interactions:
index, graph = crawl_web('http://www.udacity.com/cs101x/index.html')
ranks = compute_ranks(graph)
print lucky_search(index, ranks, 'enough')























