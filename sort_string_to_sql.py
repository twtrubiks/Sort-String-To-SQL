import re

'''
Convert Sort Expression to SQL

Converts 'sort format' to 'SQL format'. E.g.:

'id'  -> 'id ASC'
'+id'  -> 'id ASC'
'-id' -> 'id DESC'
'+id,-name'  -> 'id ASC, name DESC'
'-id,+age,-name'  -> 'id DESC, age ASC, name DESC'

(See tests.py for more examples.)

'''


def convert_one_sort_str_field_to_sql(sort_str):
    sort_str_format = '([+-])?([\w.]+)'
    sort_str = sort_str.strip()
    parsed = re.match(sort_str_format, sort_str)
    if parsed is None:
        return ''

    order = 'DESC' if parsed.group(1) == '-' else 'ASC'
    field = parsed.group(2)
    return '{} {}'.format(field, order)


def sort_str_to_sql(**kwargs):
    sort_expression = kwargs.get('sort_expression')
    if not isinstance(sort_expression, str):
        return ''
    content = sort_expression.split(',')
    seqs = list(map(convert_one_sort_str_field_to_sql, content))  # python3
    # int_seqs = map(convert_one_sort_str_field_to_sql, content)  # python2
    result = ', '.join(seqs)

    return result


if __name__ == "__main__":
    '''
    examples
    '''
    print('+id ->', sort_str_to_sql(sort_expression='+id'))
    print('+id,-name ->', sort_str_to_sql(sort_expression='+id,-name'))
    print(' ->', sort_str_to_sql(sort_expression=''))
