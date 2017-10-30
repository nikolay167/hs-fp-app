#query_string='Alex went to the rest'
def process_user_query(query_string):
    split_func=query_string.split()
    if split_func.isupper():
        return (f'HI{split_func}!' )

    #split_func=query_string.split()
    #greetings=[i for i in split_func]
    #return greetings



    #return [f'HI{name}!' for name in query_string.split()]
