def process_user_query(query_string):
    if len(student_names) == 0:
        return 'No studets '
    result= ''
    for name in query_string:
        result = result + ' ' +name
    return result
