#query_string='Alex went to the rest'
#query_string='Alex is my Best Friend '


def process_user_query(query_string):
    while True:
        try :
            words = ['Nikolay', 'Nishit', 'Alex', 'Catalina', 'Leo', 'OVER', 'the', 'Lazy', 'DOG']
            for word in query_string.split():
                for i in words:
                    if word==i:
                        return (f'Hi {word}')
                    else:
                        return('Sorry try again ')



#def process_user_query(query_string):

        #for line in query_string:
        #words = []
        #for word in line.split():
            #if word[0].upper():
            #    return(words.append(word))
            #    print(words)


    #split_func=query_string.split()
    #greetings=[i for i in split_func]
    #return greetings



    #return [f'HI{name}!' for name in query_string.split()]
