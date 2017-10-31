import re
def process_user_query(query_string):
    from urllib.request import urlopen

    url = query_string

# get a handler of a webpage located at the url.
    f = urlopen(url)

# read page contents
    web_page_contents = f.read().decode('utf-8')

# gentleman's rule: if you opened something, and don’t need this any more, then close it!
    f.close()
    re.compile(r'href *= *"([^"]*)"').findall(web_page_contents)[:10]
    return (re.compile)
