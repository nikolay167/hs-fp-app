def process_user_query(query_string):
    m = []
    names = {'Alex', 'Mike', 'Tessa','Nikolay','Kirill', 'Radu','Catalina','Bob'}
    for i in query_string.split():
        for name in names:
            if i == name:
                m.append(f'Hi {i}')
                break
    return m
