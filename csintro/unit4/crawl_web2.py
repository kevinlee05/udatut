def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        pageurl = tocrawl.pop()
        if pageurl not in crawled:
            content = get_page(page)
            add_page_to_index(index, pageurl, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return crawled
