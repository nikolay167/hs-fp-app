
def process_user_query(query_string):
    #split_func=query_string.split()
    #greetings=[i for i in split_func]
    #return greetings
    return [f'HI{name}!' for name in query_string()]
