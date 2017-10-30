
def process_user_query(query_string):
    words = []
    #query_string='Alex went to the rest'
    #split_func=query_string.split()
    #greetings=[i for i in split_func]
    #return greetings
    for line in query_string:
        for word in line.split():
            if word[0].isupper():
                words.append(word)
    for word in sorted(set(words)):
        return (f'HI{word}!')


    #return [f'HI{name}!' for name in query_string.split()]
