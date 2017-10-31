#query_string='Alex went to the rest'
#query_string='Bob is my Best Friend also Catalina '


def process_user_query(q):
    for word in query_string.split():
        words = ['Nikolay', 'Nishit', 'Alex', 'Catalina', 'Alex', 'Bob', 'the', 'Lazy', 'DOG']
        #print(query_string)
        for i in words:
            if word==i:
                #print(i)


                for b in word:
                    if len(b)==0:
                        if word==i:
                            return (f'Hi {word}')
                        #return (f'Hi {word}')
                    #return (f'Hi {word}')
        #return (f'Hi {word}')
        #return (f'Hi {word}')
#return (f'Hi {word}')

print(process_user_query('Bob is my Best Friend also Catalina' ))



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
