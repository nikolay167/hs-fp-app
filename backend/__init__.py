import re
import numpy as np
def process_user_query(query_string):
    from urllib.request import urlopen

    url = query_string

# get a handler of a webpage located at the url.
    f = urlopen(url)

# read page contents
    web_page_contents = f.read().decode('utf-8')

# gentleman's rule: if you opened something, and don’t need this any more, then close it!
    f.close()
    word_apple_Computer_Model = re.compile( r'<h2 class="as-bundleselection-modeltitle">\s*[A-Za-z]+ [A-Za-z]+\s*</h2>' )
    word_apple_model_Specs = re.compile( r' <h3 class="as-macbundle-modelvariationtitle">[1-9-A-Za-z]+ [a-z]+ [A-Za-z]+ [A-Z]+</h3>' )
    word_apple_Computer_price = re.compile( r'<span> \s*\S*\s* </span>' )

    #Applist = word_apple_model.findall(web_page_contents)
    Applist1 = word_apple_Computer_price.findall(web_page_contents)
    #my_var={}
    #for n in applist
    #    my_var[n]='charecteristics'
    return Applist1
