#query_string='Alex went to the rest'
def process_user_query(query_string):
    for line in query_string:
        words = []
        for word in line.split():
            if word[0].isupper():
                return(words.append(word))



    #split_func=query_string.split()
    #greetings=[i for i in split_func]
    #return greetings



    #return [f'HI{name}!' for name in query_string.split()]
