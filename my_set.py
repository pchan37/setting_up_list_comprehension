def union(set_a, set_b):
    return [value for index, value in enumerate(set_a) if value not in set_a[:index]] + (
        [value for index, value in enumerate(set_b) if value not in set_a and value not in set_b[:index]]
    )

def intersection(set_a, set_b):
    return [value for index, value in enumerate(set_a) if value not in set_a[:index] and value in set_b]

def set_difference(set_a, set_b):
    return [value for index, value in enumerate(set_a) if value not in set_a[:index] and value not in set_b]

def symmetric_difference(set_a, set_b):
    return set_difference(union(set_a, set_b), intersection(set_a, set_b))

def cartesian_product(set_a, set_b):
    unique_set_a = [value for index, value in enumerate(set_a) if value not in set_a[:index]]
    unique_set_b = [value for index, value in enumerate(set_b) if value not in set_b[:index]]
    return [(value_a, value_b) for value_a in unique_set_a for value_b in unique_set_b]

if __name__ == '__main__':
    print 'Please run unit_test.py where the functions are tested...  Thank you!'

