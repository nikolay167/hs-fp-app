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
    word_apple_model = re.compile( r'<h2 class="as-bundleselection-modeltitle">\s*[A-Za-z]+ [A-Za-z]+\s*</h2>' )
    Applist = word_apple_model.findall(web_page_contents)
    my_var=[]
    return my_var.append(Applist)
