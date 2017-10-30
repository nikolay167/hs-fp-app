
def process_user_query(query_string):
    split_func=query_string.split()
    greetings=[]
    for i in split_func:
        greetings.append(f'HI!  {i}')
    return greetings
