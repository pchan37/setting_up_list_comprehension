from itertools import product
from random import sample
from sys import stdout

from my_set import union, intersection, set_difference, symmetric_difference, cartesian_product

'''
Time to write unit test to test the code nice and proper...
'''

NUM_TESTS = 1000

def test_union():
    print 'Testing union...   ',
    stdout.flush()
    for i in xrange(NUM_TESTS):
        test_set_a = [i for i in sample(xrange(50), 20) for _ in xrange(20)]
        test_set_b = [i for i in sample(xrange(40, 90), 20) for _ in xrange(20)]
        assert sorted(union(test_set_a, test_set_b)) == sorted(list(set.union(set(test_set_a), set(test_set_b)))), (
            'Union calculated incorrectly!'
        )
    print 'Passed!'

def test_intersection():
    print 'Testing intersection...   ',
    stdout.flush()
    for i in xrange(NUM_TESTS):
        test_set_a = [i for i in sample(xrange(50), 20) for _ in xrange(20)]
        test_set_b = [i for i in sample(xrange(40, 90), 20) for _ in xrange(20)]
        assert sorted(intersection(test_set_a, test_set_b)) == sorted(list(set.intersection(set(test_set_a), set(test_set_b)))), (
            'Intersection calculated incorrectly!'
        )
    print 'Passed!'

def test_set_difference():
    print 'Testing set difference...   ',
    stdout.flush()
    for i in xrange(NUM_TESTS):
        test_set_a = [i for i in sample(xrange(50), 20) for _ in xrange(20)]
        test_set_b = [i for i in sample(xrange(40, 90), 20) for _ in xrange(20)]
        assert sorted(set_difference(test_set_a, test_set_b)) == sorted(list(set.difference(set(test_set_a), set(test_set_b)))), (
            'Set difference calculated incorrectly!'
        )
    print 'Passed!'

def test_symmetric_difference():
    print 'Testing symmetric difference...   ',
    stdout.flush()
    for i in xrange(NUM_TESTS):
        test_set_a = [i for i in sample(xrange(50), 20) for _ in xrange(20)]
        test_set_b = [i for i in sample(xrange(40, 90), 20) for _ in xrange(20)]
        assert sorted(symmetric_difference(test_set_a, test_set_b)) == sorted(list(set(test_set_a) ^ set(test_set_b))), (
            'Symmetric difference calculated incorrectly!'
        )
    print 'Passed!'

def test_cartesian_product():
    print 'Testing cartesian product...   ',
    stdout.flush()
    for i in xrange(NUM_TESTS):
        test_set_a = [i for i in sample(xrange(50), 20) for _ in xrange(20)]
        test_set_b = [i for i in sample(xrange(40, 90), 20) for _ in xrange(20)]
        assert sorted(cartesian_product(test_set_a, test_set_b)) == sorted(list(product(set(test_set_a), set(test_set_b)))), (
            'Cartesian product calculated incorrectly!'
        )
    print 'Passed!'

def main():
    print 'Running the unit test for all functions:\n'
    test_union()
    test_intersection()
    test_set_difference()
    test_symmetric_difference()
    test_cartesian_product()

if __name__ == '__main__':
    main()
